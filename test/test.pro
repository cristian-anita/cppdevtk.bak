#****************************************************************************************************************************
# Copyright (C) 2015 - 2020 CoSoSys Ltd <info@cososys.com>
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# Please see the file COPYING.
#
# Author(s): Cristian ANITA <cristian.anita@cososys.com>, <cristian_anita@yahoo.com>
#****************************************************************************************************************************


TEMPLATE = subdirs


include(./../common.pri)


#CONFIG *= ordered


SUBDIRS +=	\
	test_base	\
	test_caps_lock_widget	\
	test_config	\
	test_disk_space_widget	\
	test_invisible_widget	\
	test_localization	\
	test_slot_throw	\
	test_term_sig	\
	test_util
	
!android:!ios {
	SUBDIRS += test_pc_man
}

isEqual(CPPDEVTK_ENABLE_QTSOLUTIONS, "true") {
	SUBDIRS +=	\
		test_service	\
		test_service_controller
	
	test_service_controller.depends = test_service
}
