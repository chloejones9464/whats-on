<script type="text/javascript">  
var myWidget = cloudinary.createUploadWidget({
  cloudName: 'dcvyln5fy', 
  uploadPreset: 'media_upload'}, (error, result) => { 
    if (!error && result && result.event === "success") { 
      console.log('Done! Here is the image info: ', result.info); 
    }
  }
)

document.getElementById("upload_widget").addEventListener("click", function(){
    myWidget.open();
  }, false);
</script>

