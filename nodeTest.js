// Imports the Google Cloud client library
const vision = require('@google-cloud/vision');



//var path = require('path');
//path.dirname('swamphack2019-9f9ff1b7129f.json');


// Creates a client
const client = new vision.ImageAnnotatorClient();

// Performs label detection on the image file
client
  .labelDetection('beach.jpg')
  .then(results => {
    const labels = results[0].labelAnnotations;

    console.log('Labels:');
    labels.forEach(label => console.log(label.description));
  })
  .catch(err => {
    console.error('ERROR:', err);
  });