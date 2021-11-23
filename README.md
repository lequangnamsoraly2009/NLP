# NLP - Nhập Môn Xử Lý Ngôn Ngữ Tự Nhiên
 // Show Error
      // const error_fullname = document.getElementById("err_fullname");
      // const error_username = document.getElementById("err_username");
      // const error_email = document.getElementById("err_email");
      // const error_phone = document.getElementById("err_phone");
      // const error_birth = document.getElementById("err_birth");
      // const error_password = document.getElementById("err_password");
      // const error_confirmpassword = document.getElementById(
      //   "err_confirmpassword"
      // );
      // Value Form
      // const fullname = document.getElementById("fullname").value;
      // const username = document.getElementById("username").value;
      // const email = document.getElementById("email").value;
      // const phoneNumber = document.getElementById("phoneNumber").value;
      // const birthDay = document.getElementById("birthDay").value;
      // const password = document.getElementById("password").value;
      // const confirmPassword = document.getElementById("confirmPassword").value;

      // Regex Check
      // const regexFullName = /(\b[A-Z](?!\s))/g;
      // const regexUserName = /^[a-zA-Z0-9]+$/;
      // const regexEmail = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
      // const regexPhone = /^[0-9]{10}$/;
      // const regexBirth = /^[0-9]{4}-[0-9]{2}-[0-9]{2}$/;
      // const year = birthDay.split("-")[0];
      // const regexPass = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/;

      // const validationForm = () => {
      //   // validate fullname
      //   if (fullname.match(regexFullName)) {
      //     error_fullname.innerHTML = "Full Name required capitalize!";
      //     return false;
      //   }
      //   // validate username
      //   if (username.match(regexUserName)) {
      //     error_username.innerHTML = "Username must be alphanumeric!";
      //     return false;
      //   }
      //   // validate email
      //   if (email.match(regexEmail)) {
      //     error_email.innerHTML = "Email invalid!";
      //     return false;
      //   }
      //   // validate phone
      //   if (phoneNumber.match(regexPhone)) {
      //     error_phone.innerHTML = "Phone invalid!";
      //     return false;
      //   }
      //   // validate birthday
      //   if (
      //     birthDay.match(regexBirth) &&
      //     2021 - parseInt(year) >= 15 &&
      //     2021 - parseInt(year) <= 55
      //   ) {
      //     error_birth.innerHTML =
      //       "Birthday is invalid and age is in the range [15,55] !";
      //     return false;
      //   }
      //   // validate password
      //   if (password.match(regexPass)) {
      //     error_password.innerHTML =
      //       "Password must be at least 8 characters, one letter and one number!";
      //     return false;
      //   }
      //   // validate confirm password
      //   if (password !== confirmPassword) {
      //     error_confirmpassword.innerHTML = "Password not match!";
      //     return false;
      //   }
      // };

      // event handler functions
      // const fullnameVerify = () => {
      //   if (fullname === "") {
      //     error_fullname.innerHTML = "Full Name required!";
      //     return false;
      //   } else {
      //     error_fullname.innerHTML = "";
      //     return true;
      //   }
      // };
      // const usernameVerify = () => {
      //   if (username === "") {
      //     error_username.innerHTML = "Username required!";
      //     return false;
      //   } else {
      //     error_username.innerHTML = "";
      //     return true;
      //   }
      // };
      // const emailVerify = () => {
      //   if (email === "") {
      //     error_email.innerHTML = "Email required!";
      //     return false;
      //   } else {
      //     error_email.innerHTML = "";
      //     return true;
      //   }
      // };
      // const phoneVerify = () => {
      //   if (phoneNumber === "") {
      //     error_phone.innerHTML = "Phone required!";
      //     return false;
      //   } else {
      //     error_phone.innerHTML = "";
      //     return true;
      //   }
      // };
      // const birthVerify = () => {
      //   if (birthDay === "") {
      //     error_birth.innerHTML = "Birthday required!";
      //     return false;
      //   } else {
      //     error_birth.innerHTML = "";
      //     return true;
      //   }
      // };
      // const passwordVerify = () => {
      //   if (password === "") {
      //     error_password.innerHTML = "Password required!";
      //     return false;
      //   } else {
      //     error_password.innerHTML = "";
      //     return true;
      //   }
      // };
      // const confirmPasswordVerify = () => {
      //   if (confirmPassword === "") {
      //     error_confirmpassword.innerHTML = "Confirm Password required!";
      //     return false;
      //   } else {
      //     error_confirmpassword.innerHTML = "";
      //     return true;
      //   }
      // };
      // // Setting all event listener
      // document
      //   .getElementById("fullname")
      //   .addEventListener("blur", fullnameVerify);
      // document
      //   .getElementById("username")
      //   .addEventListener("blur", usernameVerify);
      // document.getElementById("email").addEventListener("blur", emailVerify);
      // document
      //   .getElementById("phoneNumber")
      //   .addEventListener("blur", phoneVerify);
      // document.getElementById("birthDay").addEventListener("blur", birthVerify);
      // document
      //   .getElementById("password")
      //   .addEventListener("blur", passwordVerify);
      // document
      //   .getElementById("confirmPassword")
      //   .addEventListener("blur", confirmPasswordVerify);