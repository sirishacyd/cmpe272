# CMPE 272: serverless
* University Name: San Jose State University http://www.sjsu.edu/ 
* Student: [Sirisha Polisetty](https://www.linkedin.com/in/sirishapolisetty/)
### Media processing serverless Application

* Media processing application that allows us to analyze images and videos to detect real world objects in media files. The results of the analysis can then be quierried through the REST API.

### Architecture Diagram

* For the image processing once we upload image in s3 bucket lambda function will invoke and image will be processed using amazon rekognition once it’s done add image lambda function will store labels date from amazon recognition into dynamo DB. 

* For the video processing once we upload a video file into s3 bucket lambda function will invoke and video will be processed using amazon rekognition then  one message notification will be triggered in SNS. Once  it’s done, the video lambda function will store labels from amazon rekognition into dynamo DB . 

* App handler lambda function is invoked via api gateway which queries data stored in dynamo DB and responds to users with data about labels that are created from media processing.

### sample files to do the media processing

* Open the lambda function using https URL.
* https://w2p71mpvp5.execute-api.us-west-1.amazonaws.com/api?media-type=image

* https://w2p71mpvp5.execute-api.us-west-1.amazonaws.com/api?media-type=video

* https://w2p71mpvp5.execute-api.us-west-1.amazonaws.com/api?startswith=sam

* https://w2p71mpvp5.execute-api.us-west-1.amazonaws.com/api?label=Person




  

