 const modal = document.getElementById('search-modal');
 const closeBtn = document.getElementsByClassName('close')[0];
 const trackingInput = document.getElementById('tracking-code');
 const shippingInput = document.getElementById('shipping-details');


 function handleSearch() {
    if (trackingInput.value.trim() || shippingInput.value.trim()) {
        modal.style.display = "flex";
    }
 }

 window.onload = function() {
    modal.style.display = "none";
 }

 closeBtn.onClick = function() {
    modal.style.display = "none";
 }

window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
 }

closeBtn.onclick = function() {
    modal.style.display = "none";
};
