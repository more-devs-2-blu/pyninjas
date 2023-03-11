let modalQt = 1;
let cart = [];
let modalKey = 0;

const c = function (el) {
    return document.querySelector(el);
}

const cs = function (el) {
    return document.querySelectorAll(el);
}


//Listagem das pizzas
const mostraTudo = async () => {
    const response = await fetch('http://127.0.0.1:8000/item/');
    let pizzaJson = await response.json(); //extract JSON from the http response
    
    pizzaJson.forEach(item => 
        item["sizes"] = ['Pequena', 'Média', 'Grande']
    )

    pizzaJson
    console.log(pizzaJson)

    pizzaJson.map((item, index) => {
        let pizzaItem = c('.models .pizza-item').cloneNode(true);

        console.log(pizzaItem)

        
        pizzaItem.setAttribute('data-key', index);

        pizzaItem.querySelector('.pizza-item--img img').src = "images/"+ item.image;
        pizzaItem.querySelector('.pizza-item--price').innerHTML = `R$ ${item.price.toFixed(2)}`;
        pizzaItem.querySelector('.pizza-item--name').innerHTML = item.name;
        pizzaItem.querySelector('.pizza-item--desc').innerHTML = item.description;
        pizzaItem.querySelector('a').addEventListener('click', (e)=>{
            e.preventDefault();

            modalQt = 1;

            let key = e.target.closest('.pizza-item').getAttribute('data-key');

            modalKey = key;

            c('.pizzaBig img').src = "images/"+ pizzaJson[key].image;
            c('.pizzaInfo h1').innerHTML = pizzaJson[key].name;
            c('.pizzaInfo--desc').innerHTML = pizzaJson[key].description;
            c('.pizzaInfo--actualPrice').innerHTML = `R$ ${pizzaJson[key].price.toFixed(2)}`;
            c('.pizzaInfo--size.selected').classList.remove('selected');
            cs('.pizzaInfo--size').forEach((size, sizeIndex) => {
                if(sizeIndex == 2) {
                    size.classList.add('selected');
                };
                size.querySelector('span').innerHTML = pizzaJson[key].sizes[sizeIndex];
            });

            c('.pizzaInfo--qt').innerHTML = modalQt;

            c('.pizzaWindowArea').style.opacity = 0;
            c('.pizzaWindowArea').style.display = 'flex';
            setTimeout(()=>{
                c('.pizzaWindowArea').style.opacity = 1;
            }, 200);



        });
        
        c('.pizza-area').append(pizzaItem);
    });
}

mostraTudo()


//Eventos do Modal
function closeModal() {
    c('.pizzaWindowArea').style.opacity = 0;
    setTimeout (() => {
        c('.pizzaWindowArea').style.display = 'none';
    }, 500);
}

cs('.pizzaInfo--cancelButton, .pizzaInfo--cancelMobileButton').forEach((item) => {
    item.addEventListener('click', closeModal);
});

c('.pizzaInfo--qtmenos').addEventListener('click', ()=>{
    if(modalQt > 1) {
        modalQt--;
        c('.pizzaInfo--qt').innerHTML = modalQt;
    } 
}); 

c('.pizzaInfo--qtmais').addEventListener('click', ()=>{
    modalQt++;
    c('.pizzaInfo--qt').innerHTML = modalQt;
});

cs('.pizzaInfo--size').forEach((size, sizeIndex) => {
    size.addEventListener('click', (e) => {
        c('.pizzaInfo--size.selected').classList.remove('selected');
        size.classList.add('selected');
    });
});

c('.pizzaInfo--addButton').addEventListener('click', () => {
    let size =  parseInt(c('.pizzaInfo--size.selected').getAttribute('data-key'));

    let identifier = pizzaJson[modalKey].id+'@'+size;

    let key = cart.findIndex((item) => item.identifier == identifier);

    if(key > -1) {
        cart[key].qt += modalQt;
    } else {
        cart.push({
            identifier,
            id:pizzaJson[modalKey].id,
            size,
            qt:modalQt
        });
        
    }

    updateCart();
    closeModal();
});

c('.menu-openner').addEventListener('click', () => {
    if(cart.length > 0) {
        c('aside').style.left = '0';
    }
});
c('.menu-closer').addEventListener('click', () => {
    c('aside').style.left = '100vw';
});


function updateCart() {
    c('.menu-openner span').innerHTML = cart.length;

    if(cart.length > 0) {
        c('aside').classList.add('show');
        c('.cart').innerHTML = '';

        let subtotal = 0;
        let desconto = 0;
        let total = 0;

        for (let i in cart) {
            let pizzaItem = pizzaJson.find((item) => item.id == cart[i].id);

            subtotal += pizzaItem.price * cart[i].qt;
            
            let cartItem = c('.models .cart--item').cloneNode(true);

            let pizzaSizeName;
            switch(cart[i].size) {
                case 0:
                    pizzaSizeName = '';
                    break;
                case 1:
                    pizzaSizeName = '';
                    break;  
                case 2:
                    pizzaSizeName = '';
                    break;     
            }


            let pizzaName = `${pizzaItem.name} `;

            cartItem.querySelector('img').src = pizzaItem.img;
            cartItem.querySelector('.cart--item-nome').innerHTML = pizzaName;
            cartItem.querySelector('.cart--item--qt').innerHTML = cart[i].qt;
            cartItem.querySelector('.cart--item-qtmenos').addEventListener('click', () => {
                if(cart[i].qt > 1) {
                    cart[i].qt--;
                } else {
                    cart.splice(i, 1);
                }
                updateCart ();
            });
            cartItem.querySelector('.cart--item-qtmais').addEventListener('click', () => {
                cart[i].qt++;
                updateCart ();
            });

            c('.cart').append(cartItem);
        }

        desconto = subtotal * 0.1;
        total = subtotal + desconto;

        c('.subtotal span:last-child').innerHTML = `${subtotal.toFixed(2)}`;
        c('.desconto span:last-child').innerHTML = `${desconto.toFixed(2)}`;
        c('.total span:last-child').innerHTML = `${total.toFixed(2)}`;
        
    } else {
        c('aside').classList.remove('show');
        c('aside').style.left= '100vw';
    }
}