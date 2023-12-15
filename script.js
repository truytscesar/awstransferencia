function uploadFile() {
    var file = document.getElementById('fileToUpload').files[0];
    var presignedUrl = 'https://videos-aus-ouvidos.s3.amazonaws.com/fotos.jpeg?AWSAccessKeyId=AKIAYIKCTZ2IPFMDFY4Q&Signature=Wsrf43ZbT52LAHy4XyySPcDG%2Bbo%3D&Expires=1702676554'
        // Verifica se um arquivo foi selecionado
    if (!file) {
        alert('Por favor, selecione um arquivo para fazer upload.');
        return;
    }

    var xhr = new XMLHttpRequest();
    xhr.open('PUT', presignedUrl, true);
    xhr.setRequestHeader('Content-Type', file.type);

    xhr.onreadystatechange = function() {
        if(xhr.readyState === 4){
            if(xhr.status === 200){
                alert('Upload concluído com sucesso!');
            } else {
                alert('Erro no upload: ', xhr.responseText);
            }
        }
    };

    xhr.send(file);
}
