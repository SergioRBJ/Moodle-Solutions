<?php

namespace theme_fordson\output\core;
defined('MOODLE_INTERNAL') || die();

//use moodle_url;
//use html_writer;

	public function envio()
	{
		global $DB


		$auxSql  = "SELECT DISTINCT CONCAT(u.firstname,' ',u.lastname) AS nome,FROM_UNIXTIME(u.lastaccess) AS primeiro_acesso,g.name as POLO FROM ava_poliseducacional_com_br.mdl_user u ";
		$auxSql .= "INNER JOIN mdl_role_assignments ra ON ra.userid = u.id ";
		$auxSql .= "LEFT JOIN mdl_groups g ON g.id = gp.groupid ";
		$auxSql .= "WHERE FROM_UNIXTIME(u.lastaccess) > '2018-01-01' ";
		$auxSql .= "AND DATEDIFF( NOW(),FROM_UNIXTIME(`lastaccess`) ) > 7  ";
		$auxSql .= "AND ra.roleid = 5 ";
		$auxSql .= "AND g.name LIKE '%POLO%' ";
		$auxSql .= "ORDER BY u.firstname";
		$auxArray = $DB->get_records_sql($auxSql);	

    }
