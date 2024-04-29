$('.fileContainer').each(function() {
  $(this).find('input[type="file"]').change(event => {
    let arquivos = event.target.files;
    if (arquivos.length === 0) {
      console.log('sem imagem pra mostrar')
    } else {
        let tipoArquivo = arquivos[0].type;
        if(tipoArquivo == 'image/jpeg' || tipoArquivo == 'image/png' || tipoArquivo == 'image/gif') {
          $(this).find('.item-img img').remove();
          let imagem = $('<img height="430">');
          imagem.attr('src', window.URL.createObjectURL(arquivos[0]));
          $(this).find('.item-img').prepend(imagem);
        } else {
          alert('Formato não suportado')
        }
    }
  });
});
