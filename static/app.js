function sendAction(type) {
  xhr = new XMLHttpRequest();
  xhr.open('GET', 'car/'+type);
  xhr.onreadystatechange = function() {
    if(xhr.readyState==4 && xhr.status==200) {
      console.log(type + ' done');
    }
  }
  xhr.send(null);
}

function action(type) {
  sendAction(type);
}
