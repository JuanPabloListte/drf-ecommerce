var update_id = 0;

function addMeasureUnit(){ 
    fetchCreateUpdate('measure_unit/', {
        'description': document.getElementById('description').value
    });
}

function updateMeasureUnit(){
    let url = 'measure_unit/' + update_id + "/"
    fetchCreateUpdate(url, {
        'description': document.getElementById('id_description').value
    }, true);
}

window.actionEvents = {
    'click .btn-secondary': function(e, value, row, index){
        update_id = row.id;
        fetch(base_API + 'measure_unit/'+row.id+"/",{
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
            document.getElementById('id_description').value = data.description;
            document.getElementById('openUpdateModal').click();
        })
        .catch(function(error){
            console.log("RESPUESTA EN CATCH");
            console.log(error);
        });
    },
    'click .btn-danger': function(e, value, row, index){
        fetchDelete('measure_unit/' + row.id + "/");
    }
}