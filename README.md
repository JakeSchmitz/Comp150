Follow along in class if you want to set up a VM with a hadoop cluster 
running Cloudera's Distribution of Hadoop and run MapReduce code written
in python.

The presentation will start with a walkthrough of setting up the VM for the
demo. See the attached PDF for more thorough instructions on this step.

Next we will open up the VM and open the terminal. Inside the terminal we 
will start up Cloudera Manager which is a web interface for administering
a Hadoop Cluster. To start CM, run sudo ~/cloudera-manager --force. 

Next open up firefox and go to Cloudera Manager using the shortcut in the 
toolbar. Login with the username and password as cloudera. When the homepage
loads (which may take a while) make sure the YARN component is started in
the left hand column.  

After Confirming YARN is running, go back to the terminal and clone this 
repository if you have git set up on the VM (or know how to quickly), 
otherwise just copy and paste the code you need (only 3 files total). 

Git is already installed in the VM so the setup work amounts to 
generating a new public ssh key and registering it with git. Follow the 
instructions here if you want to clone the repo: https://help.github.com/articles/generating-ssh-keys/

Both examples work the map phase reading individual lines from the input
text and outputing a Key Value pair for each word in the line, with the
word as the key and 1 as the value. The reducer step then combines all
output from the map phase with the same key by summing the counts. The 
reduce phase then outputs Key Value pairs with unique words for the keys
and the total count of that word as the value.  

To setup both, we need to create an input directory in HDFS to store the
input files. Do this with the following command:
    hadoop fs -mkdir /user/cloudera/input

Then put the input files in the input directory in HDFS with:
    hadoop fs -put mobydick.txt /user/cloudera/input/

You can have as many files as you want in the input directory, all of which
will be fed through WordCount. 

Once the input is in HDFS, you should be able to run either example.

PYTHON
======
To run the python version, first change into the python directory.

The command is long, but here it is: 
hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-2.5.0-mr1-cdh5.2.0.jar -input /user/cloudera/input -output /user/cloudera/output -mapper /home/cloudera/path/to/mapper.py -reducer /home/cloudera/path/to/reducer.py

make sure you replace the /path/to/ parts with the paths on your local 
machine to the python folder in the cloned repository based on where you 
cloned from.

That should work, and the output will be in HDFS in /user/cloudera/output/

I find it easiest to write the results of all the files in the output
directory to a local file using the following command: 
    hadoop fs -cat /user/cloudera/output/* > results


JAVA
====
To run the java version, first change into the java directory.

Next, create a directory to write the compiled class files to.
    mkdir wordcount_classes

Then, compile Wordcount
    javac -cp /usr/lib/hadoop/*:/usr/lib/hadoop/client/* WordCount.java -d wordcount_classes/

Next, assemble the class files into a jar file with:
    jar -cvf wordcount.jar -C WordCount_classes/ .

After that you're ready to run the java version, but first make sure you've
removed the results of any previous run with:
    hadoop fs -rm -r /user/cloudera/output

Now run WordCount with this:
     hadoop jar wordcount.jar WordCount /user/cloudera/wordcount/input /user/cloudera/wordcount/output

REFERENCES
==========

1.Cloudera Hadoop Tutorial: http://www.cloudera.com/content/cloudera/en/documentation/hadoop-tutorial/CDH5/Hadoop-Tutorial.html

2. Michael Noll Python MapReduce Tutorial: http://www.michael-noll.com/tutorials/writing-an-hadoop-mapreduce-program-in-python/

3. VirtualBox VM download/ documentation: https://www.virtualbox.org/wiki/Downloads

4. Cloudera Quickstart VM Download: http://www.cloudera.com/content/cloudera/en/downloads/quickstart_vms/cdh-5-2-x.html


