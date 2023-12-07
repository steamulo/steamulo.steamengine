### Changelog

All notable changes to this project will be documented in this file. Dates are displayed in UTC.

#### [2.7.2](https://github.com/STEAMULO/steamulo.steamengine/compare/2.7.1...2.7.2)

> 6 December 2023

- [FIX] Fix on checksum verification

#### [2.7.1](https://github.com/STEAMULO/steamulo.steamengine/compare/2.7.0...2.7.1)

> 30 November 2023

- [FIX] Possiblité de renseigner un public directory drupal vide into steamengine_drupal_public_directory

### Breaking Changes

- *steamengine_drupal_public_directory* should start with slash

#### [2.7.0](https://github.com/STEAMULO/steamulo.steamengine/compare/2.6.0...2.7.0)

> 16 October 2023

- Modify the checksum verification
- [PATCH] Avoid the empty checksum bypass verification
- [UPDATE] Add the following line in the playbook of the ansible project: *steamengine_skip_checksum: "{{ steamengine_builds[stm_dpt.key].steamengine_skip_checksum | default(False) }}"*
 This line is needed to skip the verification of the checksum


#### [2.6.0](https://github.com/STEAMULO/steamulo.steamengine/compare/2.5.0...2.6.0)

> 21 March 2023

- Drupal [`#13`](https://github.com/STEAMULO/steamulo.steamengine/pull/13)
- [FIX] drupal php fpm version [`#45`](https://github.com/STEAMULO/steamulo.steamengine/pull/45)
- [FIX] remove unused variables [`#34`](https://github.com/STEAMULO/steamulo.steamengine/pull/34)
- [FIX] prefix drupal specific variables with steamengine_drupal [`#33`](https://github.com/STEAMULO/steamulo.steamengine/pull/33)
- Rename drupal variables [`#32`](https://github.com/STEAMULO/steamulo.steamengine/pull/32)
- [FIX] variable steamengine_drupal_public_directory forgotten in some … [`#28`](https://github.com/STEAMULO/steamulo.steamengine/pull/28)
- Add drupal .env file support [`#23`](https://github.com/STEAMULO/steamulo.steamengine/pull/23)
- Split tests scenario for drupal [`3f15677`](https://github.com/STEAMULO/steamulo.steamengine/commit/3f15677a6e226e2f6598edfeefddb10f58b84797)
- Refacto on drupal test [`ba6f3fe`](https://github.com/STEAMULO/steamulo.steamengine/commit/ba6f3fe8c1ae75dbe21306372bd9deb9dbce0316)
- Maj for steamengin Drupal [`bbcd5c9`](https://github.com/STEAMULO/steamulo.steamengine/commit/bbcd5c9255d1bc3b1bcd594a24b3aa3a16b6ae3e)

### Breaking Changes

- Rename *steamengine_sf_php_bin_path* to *steamengine_php_bin_path*
- Rename *steamengine_sf_php_fpm_version* to *steamengine_php_fpm_service_name*

#### [2.5.0](https://github.com/STEAMULO/steamulo.steamengine/compare/2.4.0...2.5.0)

> 8 November 2022

- Add support for pre deploy commands [`9e36003`](https://github.com/STEAMULO/steamulo.steamengine/commit/9e360037ac57da0a1c1509b4d16d73a7738f4be9)

#### [2.4.0](https://github.com/STEAMULO/steamulo.steamengine/compare/2.3.0...2.4.0)

> 10 October 2022

- Use variable for php binary path [`#43`](https://github.com/STEAMULO/steamulo.steamengine/pull/43)
- Remove unnecessary molecule preprun [`7848f0b`](https://github.com/STEAMULO/steamulo.steamengine/commit/7848f0be68a8b6ecf487577635f298717905cecd)
- [FIX]: Change location for declaration of php bin path [`16ee177`](https://github.com/STEAMULO/steamulo.steamengine/commit/16ee17777220f133599c1981003b22a7d21dcf14)
- [ADD]: Use of environment variable defining path of php binary [`de7060d`](https://github.com/STEAMULO/steamulo.steamengine/commit/de7060d2f44d136bf4cf0d7053df12e1a98aceb1)

#### [2.3.0](https://github.com/STEAMULO/steamulo.steamengine/compare/2.2.1...2.3.0)

> 12 August 2022

- Add daemon services for project [`#41`](https://github.com/STEAMULO/steamulo.steamengine/pull/41)
- Remove old Jenkinsfile [`af95f11`](https://github.com/STEAMULO/steamulo.steamengine/commit/af95f11325bd2b0226f0023c0675489a7760c35f)

#### [2.2.1](https://github.com/STEAMULO/steamulo.steamengine/compare/2.2.0...2.2.1)

> 3 August 2022

- Increase memory limit for php clear cache command [`7635358`](https://github.com/STEAMULO/steamulo.steamengine/commit/763535816c08d385f0d6658d9620ab5a45533dcd)

#### [2.2.0](https://github.com/STEAMULO/steamulo.steamengine/compare/2.1.1...2.2.0)

> 2 August 2022

- Fix steamengine bin [`#40`](https://github.com/STEAMULO/steamulo.steamengine/pull/40)
- Replace centos 8 by rockylinux 8. Add ubuntu22. Upgrade ansible (support for os detection on rocky). [`5b89b9d`](https://github.com/STEAMULO/steamulo.steamengine/commit/5b89b9d49c73d20e6c17c37d8d5a61b0b06c7948)
- [FIX] Steamengine scripts [`e6d338e`](https://github.com/STEAMULO/steamulo.steamengine/commit/e6d338e7a21e5aaf25355a74287d4b931a2edb04)
- [FIX] Steamengine scripts - Remove unnecessary instructions [`ab0cfba`](https://github.com/STEAMULO/steamulo.steamengine/commit/ab0cfba82ccd5f78e68d6f783f61dde6a00951a7)

#### [2.1.1](https://github.com/STEAMULO/steamulo.steamengine/compare/2.1.0...2.1.1)

> 27 July 2022

- Improve fixPermissions Symfony speed [`#38`](https://github.com/STEAMULO/steamulo.steamengine/pull/38)
- Fix deploy tag SF [`d63a183`](https://github.com/STEAMULO/steamulo.steamengine/commit/d63a183a9f3d7ffebd22057b9063c8cc038fa5c0)

#### [2.1.0](https://github.com/STEAMULO/steamulo.steamengine/compare/2.0.0...2.1.0)

> 7 April 2022

- [IMPR] Change pm2 conf [`#37`](https://github.com/STEAMULO/steamulo.steamengine/pull/37)
- [FEAT] Variabilization of php-fpm version [`#35`](https://github.com/STEAMULO/steamulo.steamengine/pull/35)
- [FIX] Centos8 repo [`#36`](https://github.com/STEAMULO/steamulo.steamengine/pull/36)
- Update README.md [`9f66700`](https://github.com/STEAMULO/steamulo.steamengine/commit/9f66700013c5af487a3a3a5c812f3a0204b5ef51)

### [2.0.0](https://github.com/STEAMULO/steamulo.steamengine/compare/1.5.1...2.0.0)

> 31 January 2022

- [SF][FIX] Fix permissions for links [`#22`](https://github.com/STEAMULO/steamulo.steamengine/pull/22)
- Merge pull request #12 from STEAMULO/sf [`5aa84cf`](https://github.com/STEAMULO/steamulo.steamengine/commit/5aa84cf4bc57b2df90769423c2f46c35749f7f2c)
- [EVOL] Create symfony4 steamengine [`0660992`](https://github.com/STEAMULO/steamulo.steamengine/commit/066099251df8caf283746d2bc78ec80e438fea96)
- Use group for nginx/apache instead of acl [`1a9e6da`](https://github.com/STEAMULO/steamulo.steamengine/commit/1a9e6da1b0f4fb32f8e3c3913927914fc75e9b4c)

### Breaking Changes

- Add *run_as_app_user* and *run_in_project_root_path_web* for wrapper scripts (steamengine_wrapper_scripts_extra)
- Add *run_as_app_user* and *run_in_project_root_path_web* for crons scripts (steamengine_crons)

#### [1.5.1](https://github.com/STEAMULO/steamulo.steamengine/compare/1.5.0...1.5.1)

> 30 November 2021

- Security Fix: Fixed privileges on the steamengine bin [`#30`](https://github.com/STEAMULO/steamulo.steamengine/pull/30)
- [FIX] persistent storage now works with springboot [`#27`](https://github.com/STEAMULO/steamulo.steamengine/pull/27)
- [ADD] MaxPostSize var in tomcat Connector [`#29`](https://github.com/STEAMULO/steamulo.steamengine/pull/29)
- Fix linting and doc [`7bff82e`](https://github.com/STEAMULO/steamulo.steamengine/commit/7bff82eefdaa19a038bbd56bb9910702647fe92b)
- security: fixed privileges on the steamengine bin allowing the user to modify it [`4a4e489`](https://github.com/STEAMULO/steamulo.steamengine/commit/4a4e489d0f2ebe77aeffe62ecb6473a175675366)
- Fix linting [`29ee328`](https://github.com/STEAMULO/steamulo.steamengine/commit/29ee3287eb466ea7a733cca8902d1fcd5e275158)

#### [1.5.0](https://github.com/STEAMULO/steamulo.steamengine/compare/1.4.0...1.5.0)

> 16 September 2021

- [FIX] add condition to persistent directories tasks [`#26`](https://github.com/STEAMULO/steamulo.steamengine/pull/26)
- [FIX] slash for project path - Storage persistent [`#25`](https://github.com/STEAMULO/steamulo.steamengine/pull/25)
- [ADD] symbolic link to persistant storage directories [`#24`](https://github.com/STEAMULO/steamulo.steamengine/pull/24)
- [ADD] symbolic link to persistant directories [`023fdbf`](https://github.com/STEAMULO/steamulo.steamengine/commit/023fdbf4b78f971b7cdcfb7ecb65d70a23ad09d4)
- [FIX] Slash for path and fix recurse making the pipeline failed [`9640e32`](https://github.com/STEAMULO/steamulo.steamengine/commit/9640e3264d4cd93caeebe021fdc7fb9beb4d1ebb)
- [FIX] Persistant to persistent [`be5c0a5`](https://github.com/STEAMULO/steamulo.steamengine/commit/be5c0a5fea33f35b4c30bbec6892141421177f0c)

#### [1.4.0](https://github.com/STEAMULO/steamulo.steamengine/compare/1.3.1...1.4.0)

> 26 August 2021

- Add flexible entries for steamengine wrapper [`2f7fc06`](https://github.com/STEAMULO/steamulo.steamengine/commit/2f7fc067bb72027b0ed544fbc0e8152e703892aa)
- Add generic cron support [`777def8`](https://github.com/STEAMULO/steamulo.steamengine/commit/777def85c50b24f2d709928bcb118e97b7309fc5)

#### [1.3.1](https://github.com/STEAMULO/steamulo.steamengine/compare/1.3.0...1.3.1)

> 27 May 2021

- Add fixpermissions script for nodejs as a workaround for specific project [`22d7299`](https://github.com/STEAMULO/steamulo.steamengine/commit/22d72993cf041e95a11d78fe7fd6eaf18edd6777)
- Use python from venv Jenkinsfile [`08ac0c4`](https://github.com/STEAMULO/steamulo.steamengine/commit/08ac0c456f76cc2ace129846fa6a27e7a254fda1)

#### [1.3.0](https://github.com/STEAMULO/steamulo.steamengine/compare/1.2.10...1.3.0)

> 12 May 2021

- Merge pull request #19 from STEAMULO/tomcat-9 [`10cc269`](https://github.com/STEAMULO/steamulo.steamengine/commit/10cc269931da65bfe5a76462cc6dd339889622ee)
- Upgrade molecule, ansible, python. Add test for centos8 and ubuntu20. [`ee39403`](https://github.com/STEAMULO/steamulo.steamengine/commit/ee3940309909e81dd41952763525fadd42b5daaa)
- Upgrade molecule, ansible, python. Add test for centos8 and ubuntu20. [`963e721`](https://github.com/STEAMULO/steamulo.steamengine/commit/963e7213662959eb67299a8480720fb0d3f1a94e)

#### [1.2.10](https://github.com/STEAMULO/steamulo.steamengine/compare/1.2.9...1.2.10)

> 7 January 2021

- Move steamengine_java_base_opts to defaults [`a7ba875`](https://github.com/STEAMULO/steamulo.steamengine/commit/a7ba875770b07bd028dbd17710f11b9bc25682b1)
- [FIX] string concatenation operator in templates [`a0b3ddd`](https://github.com/STEAMULO/steamulo.steamengine/commit/a0b3ddd1f871861b60973a188c0c169055982780)

#### [1.2.9](https://github.com/STEAMULO/steamulo.steamengine/compare/1.2.8...1.2.9)

> 8 October 2020

- Configuration key to add nginx in app group for nodejs deploy [`4c697d3`](https://github.com/STEAMULO/steamulo.steamengine/commit/4c697d35ac9b5e0f2862872e8eaf029a40877925)

#### [1.2.8](https://github.com/STEAMULO/steamulo.steamengine/compare/1.2.7...1.2.8)

> 6 October 2020

- Add nodejs variable that gives write permissions on directories [`601b1bd`](https://github.com/STEAMULO/steamulo.steamengine/commit/601b1bd363b9a0f74c5dfe99186c76507e18ab8d)

#### [1.2.7](https://github.com/STEAMULO/steamulo.steamengine/compare/1.2.6...1.2.7)

> 30 September 2020

- Remove double test for tomcat7 [`3261ea0`](https://github.com/STEAMULO/steamulo.steamengine/commit/3261ea0f85c5a41488c826c95ef6482f764b0a84)
- Update Java role for molecule testing [`6e971a7`](https://github.com/STEAMULO/steamulo.steamengine/commit/6e971a775593283cc0f178f78699359618616476)
- Add extra field to journald logging [`b230f4a`](https://github.com/STEAMULO/steamulo.steamengine/commit/b230f4a51646178966c7ea9e02ea5361fbcd43f6)

#### [1.2.6](https://github.com/STEAMULO/steamulo.steamengine/compare/1.2.5...1.2.6)

> 6 July 2020

- Fix play2 deployment [`614aa2d`](https://github.com/STEAMULO/steamulo.steamengine/commit/614aa2d0592e2ab469a14313dc6952e3c4cce581)

#### [1.2.5](https://github.com/STEAMULO/steamulo.steamengine/compare/1.2.4...1.2.5)

> 6 July 2020

- Fix tag play2 deployment [`fd0f81c`](https://github.com/STEAMULO/steamulo.steamengine/commit/fd0f81c7775e57ba6de461c411e3a90df5289194)

#### [1.2.4](https://github.com/STEAMULO/steamulo.steamengine/compare/1.2.3...1.2.4)

> 2 July 2020

- Add missing tag on tomcat7 deploy [`71b9de2`](https://github.com/STEAMULO/steamulo.steamengine/commit/71b9de2fd6cf4b72f01e27ef14226f95f43cc2be)

#### [1.2.3](https://github.com/STEAMULO/steamulo.steamengine/compare/1.2.2...1.2.3)

> 26 June 2020

- Fix fixpermissions command tomcat7 on first deploy [`39b4e76`](https://github.com/STEAMULO/steamulo.steamengine/commit/39b4e768358efd6c52df646e3198deff4c08a543)

#### [1.2.2](https://github.com/STEAMULO/steamulo.steamengine/compare/1.2.1...1.2.2)

> 24 June 2020

- Add missing tag steamengine_deploy_nodejs on nodejs deploy [`4d2ff92`](https://github.com/STEAMULO/steamulo.steamengine/commit/4d2ff92be5463bdb64d11691b9be4a06fc658534)

#### [1.2.1](https://github.com/STEAMULO/steamulo.steamengine/compare/1.2.0...1.2.1)

> 18 June 2020

- Add interpreter_args option for NodeJs app [`d268891`](https://github.com/STEAMULO/steamulo.steamengine/commit/d268891375be567189c9f47813aeca9790e18307)
- Fix yaml lint [`57d9461`](https://github.com/STEAMULO/steamulo.steamengine/commit/57d94612d14175907546f456558936a9d6a5bcf3)

#### [1.2.0](https://github.com/STEAMULO/steamulo.steamengine/compare/1.1.0...1.2.0)

> 17 June 2020

- Add centos 7 support [`f5ceada`](https://github.com/STEAMULO/steamulo.steamengine/commit/f5ceada7977ac718007405ee84e8c0c8d1883afc)

#### [1.1.0](https://github.com/STEAMULO/steamulo.steamengine/compare/1.0.39...1.1.0)

> 16 June 2020

- Add header and ssl check param for getting build [`00b8f57`](https://github.com/STEAMULO/steamulo.steamengine/commit/00b8f57ec3628e159e90a1da7ea83d32d1d0fae2)

#### [1.0.39](https://github.com/STEAMULO/steamulo.steamengine/compare/1.0.38...1.0.39)

> 20 March 2020

- Fix idempotence issue in nodejs [`9f21323`](https://github.com/STEAMULO/steamulo.steamengine/commit/9f213234e38afe62d4abef3f5b436737774f3439)

#### [1.0.38](https://github.com/STEAMULO/steamulo.steamengine/compare/1.0.37...1.0.38)

> 10 March 2020

- Migrate steamengine_java_base_opts to openj9 [`e57d82f`](https://github.com/STEAMULO/steamulo.steamengine/commit/e57d82fca54bd814e38ad82aeee7ab3508ffc1cf)

#### [1.0.37](https://github.com/STEAMULO/steamulo.steamengine/compare/1.0.36...1.0.37)

> 28 January 2020

- [UPDATE] Rsyslog config [`1f54ff3`](https://github.com/STEAMULO/steamulo.steamengine/commit/1f54ff34c5ffdb597a2eb3e7db1ee0abc2c6177c)

#### [1.0.36](https://github.com/STEAMULO/steamulo.steamengine/compare/1.0.35...1.0.36)

> 24 January 2020

- [IMPR] add www-data in app group for tomcat7 [`717b83f`](https://github.com/STEAMULO/steamulo.steamengine/commit/717b83f8dc1ac8147f10db030c8f5ac1cbd896e8)
- [FIX] log path nodejs [`9f8234c`](https://github.com/STEAMULO/steamulo.steamengine/commit/9f8234c073a7f3f74b2caf17605ef7ebd295360c)

#### [1.0.35](https://github.com/STEAMULO/steamulo.steamengine/compare/1.0.34...1.0.35)

> 2 December 2019

- [FIX] molecule playbook role name use MOLECULE_PROJECT_DIRECTORY [`3dbb668`](https://github.com/STEAMULO/steamulo.steamengine/commit/3dbb66850ce3f65f4fe5a235343d02160e161ec4)
- [FIX] use cluster_mode instead of cluster for default exec_mode pm2 [`0b2d241`](https://github.com/STEAMULO/steamulo.steamengine/commit/0b2d241b26abc9fe99857254e5d9b6774ef4560c)
- [FIX] travis ci label [`7b3a566`](https://github.com/STEAMULO/steamulo.steamengine/commit/7b3a5664a31de082e8e8a67353550902e64477a8)

#### [1.0.34](https://github.com/STEAMULO/steamulo.steamengine/compare/1.0.33...1.0.34)

> 14 November 2019

- [IMPR] fix linting issue [`1b73014`](https://github.com/STEAMULO/steamulo.steamengine/commit/1b73014039a8627da89b0fc66db5899bf42cc630)
- [UPDATE] README.md [`e5f69a3`](https://github.com/STEAMULO/steamulo.steamengine/commit/e5f69a3afd0eb3516d498950fcd1ff751574681a)

#### [1.0.33](https://github.com/STEAMULO/steamulo.steamengine/compare/1.0.32...1.0.33)

> 25 October 2019

- [IMPR] update to ansible 2.8.5 and molecule 2.22 [`1dfa469`](https://github.com/STEAMULO/steamulo.steamengine/commit/1dfa469197e12d32d53f1f54033602911a6004e1)
- Adding travis conf [`1d3a9c1`](https://github.com/STEAMULO/steamulo.steamengine/commit/1d3a9c1037e4e4a13571fc5787d6b75dd3006fe2)
- [IMPR] use a config file for nodejs deployment, allowing config change without root privileges [`ca68b25`](https://github.com/STEAMULO/steamulo.steamengine/commit/ca68b25585a9545b66fa03d4c9390359fb383dcc)

#### [1.0.32](https://github.com/STEAMULO/steamulo.steamengine/compare/1.0.31...1.0.32)

> 17 September 2019

- [FIX] use WorkingDirectory instead of HOME for node app [`2e4123d`](https://github.com/STEAMULO/steamulo.steamengine/commit/2e4123d2e9923a180b48f5c28a5d8e7e47b395d0)

#### [1.0.31](https://github.com/STEAMULO/steamulo.steamengine/compare/1.0.30...1.0.31)

> 17 September 2019

- [FIX] path home nodejs [`763ec7f`](https://github.com/STEAMULO/steamulo.steamengine/commit/763ec7f024266a6bb721a983c7234b077382cb3f)

#### [1.0.30](https://github.com/STEAMULO/steamulo.steamengine/compare/1.0.29...1.0.30)

> 17 September 2019

- [IMPR] do not make a diff update for nodejs and tomcat7 [`6eacec8`](https://github.com/STEAMULO/steamulo.steamengine/commit/6eacec8efb3426382853367279221fde9f149cc1)

#### [1.0.29](https://github.com/STEAMULO/steamulo.steamengine/compare/1.0.28...1.0.29)

> 16 September 2019

- [FIX] Logging with PM2 [`a8e0dea`](https://github.com/STEAMULO/steamulo.steamengine/commit/a8e0dea5db3a42b5db698bd9850127e9e09379be)

#### [1.0.28](https://github.com/STEAMULO/steamulo.steamengine/compare/1.0.27...1.0.28)

> 13 September 2019

- [IMPR] Add env config for node app [`8b48f95`](https://github.com/STEAMULO/steamulo.steamengine/commit/8b48f95bc721ffa036e435646c4a7be9bfb8c9f2)

#### [1.0.27](https://github.com/STEAMULO/steamulo.steamengine/compare/1.0.26...1.0.27)

> 15 July 2019

- [IMPR] change permission handling for tomcat and fix order in main task [`e72d6cc`](https://github.com/STEAMULO/steamulo.steamengine/commit/e72d6cc5cc15a610207ac4c564dd4ba987344662)

#### [1.0.26](https://github.com/STEAMULO/steamulo.steamengine/compare/1.0.25...1.0.26)

> 11 July 2019

- [IMPR] add option to disable VersionLoggerListener [`02d1748`](https://github.com/STEAMULO/steamulo.steamengine/commit/02d17480ae550475941177de8bd69250017b6e60)

#### [1.0.25](https://github.com/STEAMULO/steamulo.steamengine/compare/1.0.24...1.0.25)

> 11 July 2019

- [FIX] play 2 deployment [`eda1038`](https://github.com/STEAMULO/steamulo.steamengine/commit/eda103815c523d93037c5072a5cfdc3d51c808e7)

#### [1.0.24](https://github.com/STEAMULO/steamulo.steamengine/compare/1.0.23...1.0.24)

> 11 July 2019

- [IMPR] add project name in handler [`68bc5ce`](https://github.com/STEAMULO/steamulo.steamengine/commit/68bc5ceaa613622d0167335c1e222d672b8d3dcf)
- [FIX] double slash in tomcat7 url [`ebe7778`](https://github.com/STEAMULO/steamulo.steamengine/commit/ebe77783bf6da3e7260ac709141210ff0caf2227)

#### [1.0.23](https://github.com/STEAMULO/steamulo.steamengine/compare/1.0.22...1.0.23)

> 2 July 2019

- [IMPR] check if build is not empty [`0de827f`](https://github.com/STEAMULO/steamulo.steamengine/commit/0de827f2ef9499ae41951f940a7917524f28b6a5)

#### [1.0.22](https://github.com/STEAMULO/steamulo.steamengine/compare/1.0.21...1.0.22)

> 19 June 2019

- [ADD] posibility to pass an external conf file for  tomcat7 [`#5`](https://github.com/STEAMULO/steamulo.steamengine/pull/5)
- [FIX] added permissions for play + fix permissions error on tomcat7 [`#4`](https://github.com/STEAMULO/steamulo.steamengine/pull/4)
- [ADD] new scenario to test external conf template [`7c0d6ec`](https://github.com/STEAMULO/steamulo.steamengine/commit/7c0d6ec21be987c58a81ac37686b458049e2ac35)
- [FIX] mode on config files + added external conf to springboot and play [`8844f31`](https://github.com/STEAMULO/steamulo.steamengine/commit/8844f31822846c47a703b3c50b99c363fcf01b93)
- [FIX] jenkins file [`aebd2db`](https://github.com/STEAMULO/steamulo.steamengine/commit/aebd2dbad0e90c791a691f5e9c49422567135048)

#### [1.0.21](https://github.com/STEAMULO/steamulo.steamengine/compare/1.0.20...1.0.21)

> 10 June 2019

- [FEAT] play2 project type added to steamengine v2 [`#3`](https://github.com/STEAMULO/steamulo.steamengine/pull/3)
- [FIX] Mr reviews added [`c674ce3`](https://github.com/STEAMULO/steamulo.steamengine/commit/c674ce3d4523a94735ccf4ea74c602a56afb01ae)
- [FIX] MR reviews added [`39a2c5e`](https://github.com/STEAMULO/steamulo.steamengine/commit/39a2c5e069c129aac146a79e56ce3f12d9ffe36e)
- [FIX] repair springboot service conf [`86ffb23`](https://github.com/STEAMULO/steamulo.steamengine/commit/86ffb23553155640c31543890e5793edfa0cee6d)

#### [1.0.20](https://github.com/STEAMULO/steamulo.steamengine/compare/1.0.19...1.0.20)

> 6 June 2019

- [FIX] Fix permission immediately after tomcat7 build download [`#2`](https://github.com/STEAMULO/steamulo.steamengine/pull/2)
- [FIX] notify on download build [`89d4adf`](https://github.com/STEAMULO/steamulo.steamengine/commit/89d4adf4b81105cd7ae8eb78c4ad60aa833d799d)

#### [1.0.19](https://github.com/STEAMULO/steamulo.steamengine/compare/1.0.18...1.0.19)

> 20 May 2019

- [FIX] add tags always on main task [`389d746`](https://github.com/STEAMULO/steamulo.steamengine/commit/389d7468e6eb7affdc5216eb4a6fbbb84647003b)

#### [1.0.18](https://github.com/STEAMULO/steamulo.steamengine/compare/1.0.17...1.0.18)

> 17 May 2019

- [IMPR] apply tag on included tasks instead of dupclating [`d0bc4c5`](https://github.com/STEAMULO/steamulo.steamengine/commit/d0bc4c5754a09274c4d9b5365962a4094c75d300)

#### [1.0.17](https://github.com/STEAMULO/steamulo.steamengine/compare/1.0.16...1.0.17)

> 7 May 2019

- [IMPR] prefix all tag with steamengine, add tags by project type [`0127fa3`](https://github.com/STEAMULO/steamulo.steamengine/commit/0127fa33db361c3362178197cc6c18b85384a734)

#### [1.0.16](https://github.com/STEAMULO/steamulo.steamengine/compare/1.0.15...1.0.16)

> 30 April 2019

- [IMPR] add option to remove char escaping in rsyslog, true by default [`36c876e`](https://github.com/STEAMULO/steamulo.steamengine/commit/36c876e7398b16369fd49000907a3a4ee044b11c)
- [FIX] jenkinsfile cleaning [`f2ede4c`](https://github.com/STEAMULO/steamulo.steamengine/commit/f2ede4c17820c4fde99f22c229f3fb9aace4e5b0)

#### [1.0.15](https://github.com/STEAMULO/steamulo.steamengine/compare/1.0.14...1.0.15)

> 29 April 2019

- [IMPR] fix deploy permission issue when using steamengine_tomcat7_allow_insecure_write_* conf [`9cc9ce9`](https://github.com/STEAMULO/steamulo.steamengine/commit/9cc9ce9a038405631e1407882d8aa5781950b822)

#### [1.0.14](https://github.com/STEAMULO/steamulo.steamengine/compare/1.0.13...1.0.14)

> 26 April 2019

- [IMPR] keep only app log message in application.log [`345dcf9`](https://github.com/STEAMULO/steamulo.steamengine/commit/345dcf9a141fff0eec405036d939d35db86be279)

#### [1.0.13](https://github.com/STEAMULO/steamulo.steamengine/compare/1.0.12...1.0.13)

> 26 April 2019

- [IMPR] add secure to tomcat connector for ssl termination on reverse [`245f87f`](https://github.com/STEAMULO/steamulo.steamengine/commit/245f87f495889d97e815c09c33da7558f2742d0b)

#### [1.0.12](https://github.com/STEAMULO/steamulo.steamengine/compare/1.0.11...1.0.12)

> 25 April 2019

- [IMPR] add tag in tasks because include_tasks does not inherit [`eff33f7`](https://github.com/STEAMULO/steamulo.steamengine/commit/eff33f7702bcd741c1491327d232cdbf26841b5d)

#### [1.0.11](https://github.com/STEAMULO/steamulo.steamengine/compare/1.0.10...1.0.11)

> 25 April 2019

- [IMPR] rename steamengine_build_sha1_checksum to steamengine_build_checksum [`4af267d`](https://github.com/STEAMULO/steamulo.steamengine/commit/4af267dec70e08c1d1e7862d0cfee9e2b5b53c09)

#### [1.0.10](https://github.com/STEAMULO/steamulo.steamengine/compare/1.0.9...1.0.10)

> 25 April 2019

- [IMPR] assert build url only when deploying and fix TUs [`8455fb2`](https://github.com/STEAMULO/steamulo.steamengine/commit/8455fb229a2303b3719aa4bce2021326941f35cd)

#### [1.0.9](https://github.com/STEAMULO/steamulo.steamengine/compare/1.0.8...1.0.9)

> 19 April 2019

- [ADD] unsecure application write access to ROOT folder for CardiboxV6 [`#1`](https://github.com/STEAMULO/steamulo.steamengine/pull/1)

#### [1.0.8](https://github.com/STEAMULO/steamulo.steamengine/compare/1.0.7...1.0.8)

> 18 April 2019

- [IMPR] use transport web and jdk on s3 for java, oracle otn is KO... [`3a07493`](https://github.com/STEAMULO/steamulo.steamengine/commit/3a0749333ef88cd344d9ca0a4baf718d7326f826)
- [FIX] impotence on tomcat webapp persmission [`a9a69bf`](https://github.com/STEAMULO/steamulo.steamengine/commit/a9a69bfcac23fad99c73b0cf39e3a61453f3910d)

#### [1.0.7](https://github.com/STEAMULO/steamulo.steamengine/compare/1.0.6...1.0.7)

> 16 April 2019

- [IMPR] add var for tomcat7 configuration key [`db1a14e`](https://github.com/STEAMULO/steamulo.steamengine/commit/db1a14e1fe277e1efbd2e076aaee2ac4590a6067)

#### [1.0.6](https://github.com/STEAMULO/steamulo.steamengine/compare/1.0.5...1.0.6)

> 16 April 2019

- [IMPR] add support for war that write in WEB-INF dir... [`8a7a395`](https://github.com/STEAMULO/steamulo.steamengine/commit/8a7a395144795ddc0eba524b9b3289db8a8911a1)

#### [1.0.5](https://github.com/STEAMULO/steamulo.steamengine/compare/1.0.4...1.0.5)

> 12 April 2019

- [IMPR] add readme [`b3e015a`](https://github.com/STEAMULO/steamulo.steamengine/commit/b3e015ad8fe4f6f4e77f6e09eb5b8c02bb747a07)
- [IMPR] add project configuration support for tomcat7 project [`fcd8a08`](https://github.com/STEAMULO/steamulo.steamengine/commit/fcd8a08d7dd24fc6aceaf0def9daa56e9c51f10c)

#### [1.0.4](https://github.com/STEAMULO/steamulo.steamengine/compare/1.0.3...1.0.4)

> 11 April 2019

- [IMPR] add tomcat config file generation [`6cb0361`](https://github.com/STEAMULO/steamulo.steamengine/commit/6cb036114a44b22a9aecd312cc5da4514b343fa9)

#### [1.0.3](https://github.com/STEAMULO/steamulo.steamengine/compare/1.0.2...1.0.3)

> 11 April 2019

- [FIX] replace static import by dynamic one so groups vars can be used in parent include [`4e464d8`](https://github.com/STEAMULO/steamulo.steamengine/commit/4e464d8a42218c8c1fed5e8191de8a4309e51e9b)

#### [1.0.2](https://github.com/STEAMULO/steamulo.steamengine/compare/1.0.1...1.0.2)

> 11 April 2019

- [IMPR] add java opts for tomcat and springboot, use update_from_archive for tomcat deployment [`3b4bedf`](https://github.com/STEAMULO/steamulo.steamengine/commit/3b4bedf31af1450f1e125a23a3709bddd865f40d)

#### [1.0.1](https://github.com/STEAMULO/steamulo.steamengine/compare/1.0.0...1.0.1)

> 10 April 2019

- [FIX] use include_tasks instead of import_tasks so that steamengine_project_type can be defined in group vars [`109d2b1`](https://github.com/STEAMULO/steamulo.steamengine/commit/109d2b18a6d971d20506a1b56e9e49d14eb5af1e)

#### 1.0.0

> 10 April 2019

- Initial commit [`944a182`](https://github.com/STEAMULO/steamulo.steamengine/commit/944a182e784ebf90499dbf4da69baffc66a6c634)
- [IMPR] Add Jenkinsfile [`7e46f77`](https://github.com/STEAMULO/steamulo.steamengine/commit/7e46f77beff1b3197eb2e7bac6235d5c576120d4)
- [IMPR] add support for spring boot and static deployments [`04f0b9c`](https://github.com/STEAMULO/steamulo.steamengine/commit/04f0b9c8afa4ce313bd8e3123ad4cbd1803765bb)
