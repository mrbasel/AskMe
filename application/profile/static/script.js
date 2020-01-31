
var editProfile = document.getElementsByClassName('edit-profile')[0]
var imgForm = document.getElementById('change-img-form')

editProfile.addEventListener('click', function(){

  if (imgForm.style.display != 'block') {
    imgForm.style.display = 'block';
  }
  else {
    imgForm.style.display = 'none';
  }
})
