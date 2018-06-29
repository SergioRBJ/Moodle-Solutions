<?php
 
use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;

require 'C:/Users/srbjunior/vendor/autoload.php';
require 'con_db.php';


    $auxArray = Array();
    $auxTeste = Array();

    $auxalunos = Array();

    $auxSql = "SELECT DISTINCT u.firstname AS nome,u.email FROM ava_poliseducacional_com_br.mdl_user u ";
    $auxSql .= "INNER JOIN mdl_role_assignments ra ON ra.userid = u.id ";
    $auxSql .= "LEFT JOIN mdl_groups_members gp ON gp.userid = u.id ";
    $auxSql .= "LEFT JOIN mdl_groups g ON g.id = gp.groupid ";
    $auxSql .= "WHERE FROM_UNIXTIME(u.lastaccess) > '2018-02-01' ";
    $auxSql .= "AND ra.roleid = 4 ";
    $auxSql .= "AND g.name LIKE '%POLO%' ";
    $auxSql .= "ORDER BY u.firstname ";
    $auxArray = $conn->query($auxSql);  



    $auxSql3 = "SELECT DISTINCT CONCAT(u.firstname,' ',u.lastname) AS nome,FROM_UNIXTIME(u.lastaccess) as ultimo_acesso,u.email FROM ava_poliseducacional_com_br.mdl_user u ";
    $auxSql3 .= "INNER JOIN mdl_role_assignments ra ON ra.userid = u.id ";
    $auxSql3 .= "LEFT JOIN mdl_groups_members gp ON gp.userid = u.id ";
    $auxSql3 .= "LEFT JOIN mdl_groups g ON g.id = gp.groupid ";
    $auxSql3 .= "WHERE DATEDIFF( NOW(),FROM_UNIXTIME(u.lastaccess) ) > 7 ";
    $auxSql3 .= "AND FROM_UNIXTIME(u.lastaccess) > '2018-01-01'";
    $auxSql3 .= "AND ra.roleid = 5 ";
    $auxSql3 .= "AND g.name LIKE '%POLO%' ";
    $auxSql3 .= "ORDER BY u.firstname ";
    $auxAlunos = $conn->query($auxSql3);



// inicia a classe PHPMailer habilitando o disparo de exceções
$mail = new PHPMailer(true);
try
{
    // habilita o debug
    // 0 = em mensagens de debug
    // 1 = mensagens do cliente SMTP
    // 2 = mensagens do cliente e do servidor SMTP
    // 3 = igual o 2, incluindo detalhes da conexão
    // 4 = igual o 3, inlcuindo mensagens de debug baixo-nível
    $mail->SMTPDebug = 2;
     
    // utilizar SMTP
    $mail->isSMTP();
 
    // habilita autenticação SMTP
    $mail->SMTPAuth = true;
 
    // servidor SMTP
    $mail->Host = 'smtp.gmail.com'; 
 
    // usuário, senha e porta do SMTP
    $mail->Username = '';
    $mail->Password = '';
    $mail->Port = 465;
     
    // tipo de criptografia: "tls" ou "ssl"
    $mail->SMTPSecure = 'ssl';
     

    // email e nome do remetente
    $mail->setFrom('e-mail', 'nome');
     
   //email dos remetentes selecionados na consulta
    foreach ($auxTeste as $tutor) { 
     $mail->addAddress($tutor['email'], $tutor['u.firstname']);
    }   
     
    // anexa um arquivo
    //$mail->addAttachment('composer.json');
 
    // define o formato como HTML
    $mail->isHTML(true);
     
    // codificação UTF-8
    $mail->Charset = 'UTF-8';
     
    // assunto do email
    $mail->Subject = 'Alunos Inativos';
     
    // corpo do email em HTML

   $auxLayoutEmail = Array();
   $auxLayoutEmail = '

                          <a>Segue a lista de alunos que não acessam a mais de 7 dias.</a>

                          <table border="1px" cellpadding="4px" cellspacing="0 ID="alter">
                          <tr>
                          <th>NOME</th>
                          <th>E-MAIL</th>
                          <th>ULTIMO ACESSO</th>
                          </tr>

                     ';

    foreach ($auxAlunos as $aluno) { 
    
    $auxLayoutEmail .= ' 

                          <tr>
                          <td> '. $aluno['nome'] . ' </td>
                          <td> '. $aluno['email'] . '</td>
                          <td> '. $aluno['ultimo_acesso'] . '</td>
                          </tr>

                       '; 

    }   

   $auxLayoutEmail .= '</table>';

        $mail->Body = $auxLayoutEmail;
   
     
    // corpo do email em texto
    $mail->AltBody = 'Lista de Alunos';
     
    // envia o email
    $mail->send();
    mysqli_close($conn);
    echo 'Mensagem enviada com sucesso!' . PHP_EOL;
}
catch (Exception $e)
{
    echo 'Falha ao enviar email.' . PHP_EOL;
    echo 'Erro: ' . $mail->ErrorInfo . PHP_EOL;
}