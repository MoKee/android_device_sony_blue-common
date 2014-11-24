# Copyright (C) 2012 The Android Open Source Project
# Copyright (C) 2012 The MoKee OpenSource Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Custom OTA Package commands for blue"""

def FullOTA_InstallEnd(self):
  self.script.AppendExtra('package_extract_file("system/bin/fix_storage_permissions.sh", "/tmp/fix_storage_permissions.sh");')
  self.script.AppendExtra('set_metadata("/tmp/fix_storage_permissions.sh", "uid", 0, "gid", 0, "mode", 0755);')
  self.script.AppendExtra('run_program("/tmp/fix_storage_permissions.sh");')
