var id_supplier = 0;

function showForm(){
    let form = document.getElementById('expense_form');
    form.classList.remove('hide');
    loadVoucherType();
    loadPaymentType();
    loadProducts();
}

function hideForm(){
    let form = document.getElementById('expense_form');
    form.classList.add('hide');
}


function searchSupplier(){
    let error = false;
    let cuil = document.getElementById('cuil_or_business_name').value;

    if(cuil === ''){
        alert('Must enter a CUIL.')
    }else{
        let found = document.getElementById('supplier_found');
        found.classList.remove('hide');
        
        fetch(base_API + 'expense/expense/search_supplier/?cuil_or_business_name='+cuil,{
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
                'Authorization': 'Bearer ' + getToken()
            }
        })
        .then(function(response){
            if(response.status == 400)
                error = true;
            return response.json();
        })
        .then(function(data){
            console.log(data);
            if(error){
                alert(data.mensaje);
            }else{
                showForm();
                id_supplier = data.id;
                document.getElementById('id_business_name').innerHTML = data.business_name;
                document.getElementById('cuil').innerHTML = data.cuil;
                document.getElementById('id_address').innerHTML = data.address;
            }

        })
        .catch(function(error){
            console.log("RESPONSE IN CATCH");
            console.log(error);
        });
    }

}

function loadPaymentType(){
    fetch(base_API + 'expense/expense/get_payment_types/',{
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + getToken()
        }
    })
    .then(function(response){
        return response.json();
    })
    .then(function(data){
        let select;
        select = document.getElementById('payment_type');
        
        for(let i = 0; i < data.length; i++){
            let option = document.createElement('option');  
            option.value = data[i].id;
            option.text = data[i].name;
            select.add(option);
        }
    })
    .catch(function(error){
        console.log("RESPONSE IN CATCH");
        console.log(error);
    });
}

function loadVoucherType(){
    fetch(base_API + 'expense/expense/get_vouchers/',{
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + getToken()
        }
    })
    .then(function(response){
        return response.json();
    })
    .then(function(data){
        let select;
        select = document.getElementById('voucher');
        
        for(let i = 0; i < data.length; i++){
            let option = document.createElement('option');     
            option.value = data[i].id;
            option.text = data[i].name;
            select.add(option);
        }
    })
    .catch(function(error){
        console.log("RESPONSE IN CATCH");
        console.log(error);
    });
}

function loadProducts(){
    fetch(base_API + 'expense/expense/get_products/',{
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + getToken()
        }
    })
    .then(function(response){
        return response.json();
    })
    .then(function(data){
        let select;
        select = document.getElementById('product');
        
        for(let i = 0; i < data.length; i++){
            let option = document.createElement('option');      
            option.value = data[i].id;
            option.text = data[i].name;
            select.add(option);
        }
    })
    .catch(function(error){
        console.log("RESPONSE IN CATCH");
        console.log(error);
    });
}

function addNewSupplier(){
    let data = {
        'cuil': document.getElementById('new_cuil').value,
        'business_name': document.getElementById('new_business_name').value,
        'address': document.getElementById('new_address').value,
        'phone': document.getElementById('new_phone').value,
        'email': document.getElementById('new_email').value
    };

    temp_headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'Bearer ' + getToken()
    }
    temp_body = JSON.stringify(data)

    fetch(base_API + 'expense/expense/new_supplier/',{
        method: 'POST',
        headers: temp_headers,
        body: temp_body
    })
    .then(function(response){
        if(response.status == 400 || response.status == 401){
            error = true;
        }
        return response.json();
    })
    .then(function(data){
        if(error){
            showErrors(data.error);
            error = false;
        }else{
            id_supplier = data.supplier.id;
            let found = document.getElementById('supplier_found');
            found.classList.remove('hide');
            document.getElementById('id_business_name').innerHTML = data.supplier.business_name;
            document.getElementById('cuil').innerHTML = data.supplier.cuil;
            document.getElementById('id_address').innerHTML = data.supplier.address;
            //alert(data.message);
            hideErrors();
            closeCreationModal();           
        }
    })
    .catch(function(error){
        console.log("RESPONSE IN CATCH");
        console.log(error);
    });
}


function clearFields() {
    document.getElementById('voucher_number').value = '';
    document.getElementById('date').value = '';
    document.getElementById('product').value = '';
    document.getElementById('voucher').value = '';
    document.getElementById('payment_type').value = '';
    document.getElementById('quantity').value = '0';
    document.getElementById('unit_price').value = '0';
    document.getElementById('total').value = '0';
}

function addNewExpense(){
    let data = {
        'supplier': id_supplier,
        'voucher_number': document.getElementById('voucher_number').value,
        'date': document.getElementById('date').value,
        'product': document.getElementById('product').value,
        'voucher': document.getElementById('voucher').value,
        'payment_type': document.getElementById('payment_type').value,
        'quantity': document.getElementById('quantity').value,
        'unit_price': document.getElementById('unit_price').value,
        'total': document.getElementById('total').value
    };

    temp_headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'Bearer ' + getToken()
    }
    temp_body = JSON.stringify(data)

    fetch(base_API + 'expense/expense/',{
        method: 'POST',
        headers: temp_headers,
        body: temp_body
    })
    .then(function(response){
        if(response.status == 400 || response.status == 401){
            error = true;
        }
        return response.json();
    })
    .then(function(data){
        if(error){
            showErrors(data.errors);
            error = false;
        }else{
            hideErrors();
            hideForm();
            alert(data.message);
            clearFields();        
        }
    })
    .catch(function(error){
        console.log("RESPONSE IN CATCH");
        console.log(error);
    });
}

