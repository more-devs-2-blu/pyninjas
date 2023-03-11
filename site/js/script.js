const userAction = async () => {
    const response = await fetch('http://127.0.0.1:8000/order/');
    const myJson = await response.json(); //extract JSON from the http response
    console.log(myJson);
    

    myJson.forEach(element => {
        let para = document.createElement("p");
        para.innerHTML = JSON. stringify(element)
        console.log(element.status)
        
        document.getElementById("myDIV").appendChild(para);
        
    });
    return myJson;
}