const form = document.querySelector(".wrapper form"),
fullURL = form.querySelector("input"),
shortenBtn = form.querySelector("form button"),
blurEffect = document.querySelector(".blur-effect"),
popupBox = document.querySelector(".popup-box"),
infoBox = popupBox.box(".info-box"),
form2 = popupBox.querySelector("form"),
shortenURL = popupBox.querySelector("form .shorten-url"),
copyIcon = popupBox.querySelector("form .copy-icon"),
saveBtn = popupBox.querySelector("button");

form.onsubmit = (e)=>{
    e.preventDefault();
    var formElement = document.getElementById('myForm');
    var data = new FormData(formElement);
    fetch('/redirect', {
          method: 'POST',
          body: data,
        })
        .then(response => response.text())
        .then(data => {
          document.getElementById("responseArea").innerHTML = data;
        })
        .catch(error => {
          console.error(error);
        });
}

shortenBtn.onclick = ()=>{
        blurEffect.style.display = "block";
        popupBox.classList.add("show");

        //paste your url here. Like this: codingnepalweb.com/
        let domain = "http://127.0.0.1:8000/redirect/"; 
        shortenURL.value = domain + data;

        copyIcon.onclick = ()=>{
            shortenURL.select();
            document.execCommand("copy");
        }

        saveBtn.onclick = ()=>{
            form2.onsubmit = (e)=>{
            e.preventDefault();
            }
            location.reload();
        }

    
let formData = new FormData(form);
xhr.send(formData);
}