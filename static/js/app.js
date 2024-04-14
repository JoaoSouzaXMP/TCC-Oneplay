$('form').each(function() {
  $(this).find('input[type="file"]').change(event => {
    let arquivos = event.target.files;
    if (arquivos.length === 0) {
      console.log('sem imagem pra mostrar')
    } else {
        if(arquivos[0].type == 'image/jpeg') {
          $(this).find('img').remove();
          let imagem = $('<img class="img-fluid">');
          imagem.attr('src', window.URL.createObjectURL(arquivos[0]));
          $(this).find('figure').prepend(imagem);
        } else {
          alert('Formato não suportado')
        }
    }
  });
});
