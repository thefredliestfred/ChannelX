<?php
require_once('./config/cx_membersite.php');

$cxmembersite = new CXMembersite();

$cxmembersite->SetWebsiteName('channelx.com');
#Need to create an admin email for the group...
$cxmembersite->SetAdminEmail('adfred1@buffs.wtamu.edu');
#Change all this information later
$cxmembersite->InitDB(/*hostname*/'localhost',
                      /*username*/ 'username',
                      /*password*/ 'p',
                      /*database name*/ 'testdb',
                      /*table name*/ 'cxusers');

$cxmembersite->SetRandomKey('hEw3JFcB7P7pSv6');
 ?>
