import AWS from 'aws-sdk';

AWS.config.update({
  accessKeyId: '<YOUR_ACCESS_KEY>',
  secretAccessKey: '<YOUR_SECRET_ACCESS_KEY>',
  region: '<YOUR_REGION>'
});

const s3 = new AWS.S3();

export default s3;
