# CMPE 272: serverless
* University Name: San Jose State University http://www.sjsu.edu/ 
* Student: [Sirisha Polisetty](https://www.linkedin.com/in/sirishapolisetty/)

### Media processing serverless Application

* Media processing application that allows us to analyze images and videos to detect real world objects in media files. The results of the analysis can then be quierried through the REST API.

### Architecture Diagram

<img width="861" alt="Screen Shot 2022-10-22 at 7 30 46 PM" src="https://user-images.githubusercontent.com/103618216/197370283-bb02e907-9d57-411b-b6b9-3c4b350552e7.png">


* For the image processing once we upload image in s3 bucket lambda function will invoke and image will be processed using amazon rekognition once it’s done add image lambda function will store labels date from amazon recognition into dynamo DB. 

* For the video processing once we upload a video file into s3 bucket lambda function will invoke and video will be processed using amazon rekognition then  one message notification will be triggered in SNS. Once  it’s done, the video lambda function will store labels from amazon rekognition into dynamo DB . 

* App handler lambda function is invoked via api gateway which queries data stored in dynamo DB and responds to users with data about labels that are created from media processing.

### sample files to do the media processing

<img width="794" alt="Screen Shot 2022-10-22 at 7 32 52 PM" src="https://user-images.githubusercontent.com/103618216/197370330-46e5c332-aaa6-40a1-9d5a-e2b266fc7d3e.png">


* Open the lambda function using https URL.

<img width="838" alt="Screen Shot 2022-10-22 at 7 35 53 PM" src="https://user-images.githubusercontent.com/103618216/197370450-d2305357-1d46-4532-84e0-e0cfaaf7ade8.png">


<img width="806" alt="Screen Shot 2022-10-22 at 7 36 19 PM" src="https://user-images.githubusercontent.com/103618216/197370466-029317d8-0f2c-436b-8006-5e8efc012075.png">

  

