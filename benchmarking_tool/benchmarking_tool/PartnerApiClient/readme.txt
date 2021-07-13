-----------------------------------------------------------------------------------------------------------
update: jun 29 2021
Jayden Geiser

talking with the developer at emporia we have figured out that channels 1 2 3 are the mains (power going in)
	and the other channels are individual circuits 

i have update how call the get_data function so we can input a serial number, as of writing this it has not been tested as we only have one emporia device on our account

i have made a clean data function to get the date and time into the proper format and it is easier to access and read in the data frames 

made a schedual builder that show what channels have been on or off over the last x about of days. 

Can also completly ignore the emporia_class if needed 

look at demo.py to see how it runs and more details about the structure 

-----------------------------------------------------------------------------------------------------------





# Demo client for Emporia Energy's partner API
# Additional documentation and information available at: http://partner.emporiaenergy.com/
# Contact your Emporia sales representative or email us at support@emporiaenergy.com


Required Frameworks
	# OpenJava (or Oracle) 11+ SDK
		Can be installed wiht APT:
			apt install openjdk-11-jdk-headless
			
	# Google Protocol Buffers - Open Source - For more information see: https://en.wikipedia.org/wiki/Protocol_Buffers
	
		As of 05/25/2021 can be downloaded from:
			https://github.com/protocolbuffers/protobuf/releases			
		or insalled with APT: 
			apt install command: apt install -y protobuf-compiler
			
	# Java GRPC Plugin
	Download the latest Java GRPC Plugin for your OS from the mavin repo and save it to your working directory.
			https://search.maven.org/search?q=g:io.grpc
		

Windows Instructions
--------------------
# Step 1) Generate java classes from proto file
  protoc --plugin=.\protoc-gen-grpc-java-your.version-filename.EXE --proto_path=. --java_out=.\ partner_api.proto

# Step 1 - Python) Generate python from proto file
  protoc --proto_path=. --python_out=.\python partner_api.proto

# Step 2 - java) Compile command:
  javac -cp lib\*;. -d . EmporiaEnergyApiClient.java

# Step 3 - java) Run client
  java -cp lib\*;. mains.EmporiaEnergyApiClient partner.email@someplace.com partnerPw  partner-api.emporiaenergy.com



MAC/Lunix Instructions
--------------------
# Step 1) Generate java classes from proto file
  protoc --plugin=./protoc-gen-grpc-java-your.version-filename-BINARY --proto_path=. --java_out=./ partner_api.proto

# Step 1 - Python) Generate python from proto file
  sudo protoc --proto_path=. --python_out=./python partner_api.proto

# Step 2 - java) Compile command:
  sudo javac -cp lib/\*:. -d . EmporiaEnergyApiClient.java

# Step 3 - java) Run client
  java -cp .:lib/\* mains.EmporiaEnergyApiClient phart@sustainergy.ca hello12345  partner-api.emporiaenergy.com



-------------------------------------------------------------------------------------------------------
Jayden Geisler jun 15th 2021 

i have made all the extra python files so we can use this in the pollen one app 

i could not get this to work outside of this directory. 
	when trying the java command (line: 36 in get_data.py) could never find the compiled java code in the mains folder 
	i am not sure how to get around this maybe flask has something tricky to do. 

take a look at the demo.py file to see how it works and what it returns i have also made it print out graphs form there but it is commented out for now 
	look at the graphs folders for the graph screen shots for graphing examples

the get_data function still does return a pandas data frame. this is so the data is displayed clean it is easy to change it to a list or dict with 
df = df.to_dict()  to a dict 
df = df.values.tolist() to a list 

this is a good start to the api but we will need to update it at a later date


	

