<?php
require_once("./config/membersite_config.php");

if(isset($_POST['submitted'])){
  if($cxmembersite->RegisterUser()){
    $cxmembersite->RedirectToURL('thank-you.html');
  }
}
?>

<!DOCTYPE html>
<head>
  <meta http-equiv='Content-Type' content='text/html; charset=utf-8' />
  <!-- Maybe add a title next? -->
  <title>ChannelX</title>
  <link rel="STYLESHEET" type="text/css" href="style/cx_membersite.css" />
  <script type='text/javascript' src='scripts/gen_validatorv31.js'></script>
  <link rel="STYLESHEET" type="text/css" href="style/pwdwidget.css" />
  <script src="scripts/pwdwidget.js" type="text/javascript"></script>
</head>
<body>

<!-- Start form code next -->
<div id='cx_membersite'>
<form id='register' action='<?php echo $cxmembersite->GetSelfScript(); ?>' method='post' accept-charset='UTF-8'>
<fieldset >
<legend>Register</legend>

<input type='hidden' name='submitted' id='submitted' value='1'/>

<div class='short_explanation'>* required fields</div>
<input type='text'  class='spmhidip' name='<?php echo $cxmembersite->GetSpamTrapInputName(); ?>' />

<div><span class='error'><?php echo $cxmembersite->GetErrorMessage(); ?></span></div>

<div class='container'>
    <label for='name' >Your Full Name*: </label><br/>
    <input type='text' name='name' id='name' value='<?php echo $cxmembersite->SafeDisplay('name') ?>' maxlength="50" /><br/>
    <span id='register_name_errorloc' class='error'></span>
</div>

<div class='container'>
    <label for='email' >Email Address*:</label><br/>
    <input type='text' name='email' id='email' value='<?php echo $cxmembersite->SafeDisplay('email') ?>' maxlength="50" /><br/>
    <span id='register_email_errorloc' class='error'></span>
</div>

<div class='container'>
    <label for='phone number' >Phone Number*:</label><br/>
    <input type='text' name='phone number' id='phone number' value '<?php echo $cxmembersite->SafeDisplay('phone number') ?>' maxlength="10" /><br/>
    <span id='register_phonenumber_errorloc' class='error'></span>
</div>

<div class='container' style='height:80px;'>
    <label for='password' >Password*:</label><br/>
    <div class='pwdwidgetdiv' id='thepwddiv' ></div>
    <noscript>
    <input type='password' name='password' id='password' maxlength="50" />
    </noscript>
    <div id='register_password_errorloc' class='error' style='clear:both'></div>
</div>

<div class='container'>
    <input type='submit' name='Submit' value='Submit' />
</div>

</fieldset>
</form>

<!-- client-side Form Validations-->

<script type='text/javascript'>
// <![CDATA[
    var pwdwidget = new PasswordWidget('thepwddiv','password');
    pwdwidget.MakePWDWidget();

    var frmvalidator  = new Validator("register");
    frmvalidator.EnableOnPageErrorDisplay();
    frmvalidator.EnableMsgsTogether();
    frmvalidator.addValidation("name","req","Please provide your name.");

    frmvalidator.addValidation("email","req","Please provide your email address.");

    frmvalidator.addValidation("email","email","Please provide a valid email address.");

    frmvalidator.addValidation("phone number", "phone number", "Please provide a valid phone number.");

    frmvalidator.addValidation("password","req","Please provide a password.");

// ]]>
</script>

<!--
Form Code End (see html-form-guide.com for more info.)
-->

</body>
</html>
