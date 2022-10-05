let foodID = [];
let foodName = [];
let foodPrice = [];
let sum = 0;

function hideCart() {
    $("#modal-window").addClass('hide-modal');
}
function openCart() {
    $("#modal-window").removeClass('hide-modal');
}

function changeButtonOptions(button, action) {
    if(action === 'adding') {
        $("#"+ button).attr('disabled', true);
        $("#"+ button).html('In cart');
    }
    if(action === 'removing') {
        $("#"+ button).attr('disabled', false);
        $("#"+ button).html('Add to cart');
    }
}

function addToCart(e) {
    const food = e.value.split(' ');
    foodID.push(food[0]);
    foodName.push(food[1]);
    foodPrice.push(food[2]);

    changeButtonOptions(food[0], 'adding');

    $('#show-cart-button').html("Show cart " + "<h3>[" + foodID.length + "]</h3>");
    $('#show-cart-button').addClass('show');
    $("#food-cart").append(`<div class="order-dish"><h2>` + food[1] + `</h2> <h2>$` + food[2] + `</h2></div>`);
    
    sum = sum + parseInt(food[2]);
    $("#amount").html('<h2 class="amount">Amount: $' + sum + "</h2>");
}