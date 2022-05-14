$(document).ready(() => {
  let encrypt = $(".encrypt");
  let decrypt = $(".decrypt");

  let = encryptForm = $("#encryptform");
  let = decryptForm = $("#decryptform");

  decryptForm.hide();

  encrypt.click(() => {
    decrypt.removeClass("active");
    encrypt.addClass("active");

    encryptForm.show();
    decryptForm.hide();
  });

  decrypt.click(() => {
    encrypt.removeClass("active");
    decrypt.addClass("active");

    encryptForm.hide();
    decryptForm.show();
  });
});
