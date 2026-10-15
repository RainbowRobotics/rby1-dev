# Open Source License Notices

RB-Y1 software uses the open-source libraries, fonts, and runtime components
listed below. Each component is subject to its copyright holders' license terms
and notice requirements.

Version information is based on the software inventory dated August 20, 2026,
and may vary between software releases. A dash (`—`) indicates that the inventory
does not specify a version.

## Components

| Component | Version | License | Project and contributors |
| --- | --- | --- | --- |
| [Eigen3](https://gitlab.com/libeigen/eigen) | 3.4.0 | [MPL-2.0][mpl] | Eigen project and contributors |
| [gRPC](https://github.com/grpc/grpc) | RPC: 1.54.3; SDK: 1.72.0 | [Apache-2.0][apache] | gRPC authors |
| [concurrentqueue](https://github.com/cameron314/concurrentqueue) | 1.0.4 | [BSD-2-Clause][bsd2] | Cameron Desrochers |
| [bshoshany-thread-pool](https://github.com/bshoshany/thread-pool) | 3.5.0 | [MIT][mit] | Barak Shoshany |
| [nlohmann_json](https://github.com/nlohmann/json) | 3.11.3 | [MIT][mit] | Niels Lohmann and contributors |
| [yaml-cpp](https://github.com/jbeder/yaml-cpp) | 0.8.0 | [MIT][mit] | Jesse Beder and contributors |
| [FreeType](https://freetype.org/) | 2.11.1 | [FTL][ftl] OR [GPL-2.0-or-later][gpl2] | The FreeType Project |
| [spdlog](https://github.com/gabime/spdlog) | 1.12.0 | [MIT][mit] | Gabi Melman and contributors |
| [libudev](https://github.com/systemd/systemd) | — | [LGPL-2.1-or-later][lgpl21] | systemd / udev contributors |
| [Vue](https://github.com/vuejs/core) | 3.4.31 | [MIT][mit] | Vue contributors |
| [Vuetify](https://github.com/vuetifyjs/vuetify) | 3.6.11 | [MIT][mit] | John Leider and contributors |
| [three.js](https://github.com/mrdoob/three.js) | 0.178.0 | [MIT][mit] | three.js authors |
| [urdf-loader](https://github.com/gkjohnson/urdf-loaders) | 0.12.6 | [MIT][mit] | Garrett Johnson and contributors |
| [Tweakpane](https://github.com/cocopon/tweakpane) | 4.0.5 | [MIT][mit] | Hiroki Kokubun and contributors |
| [vue-joystick-component](https://www.npmjs.com/package/vue-joystick-component) | 0.1.3 | [MIT][mit] | Package contributors |
| [Axios](https://github.com/axios/axios) | 1.7.7 | [MIT][mit] | Axios contributors |
| [@mdi/font](https://github.com/Templarian/MaterialDesign-Webfont) | 7.4.47 | [Asset-specific license terms][mdi] | Pictogrammers / Austin Andrews and contributors |
| [roboto-fontface](https://github.com/choffmeister/roboto-fontface) | — | [Apache-2.0][apache] | Google / Roboto contributors |
| [uuid](https://github.com/uuidjs/uuid) | 11.0.3 | [MIT][mit] | uuid contributors |
| [core-js](https://github.com/zloirock/core-js) | 3.37.1 | [MIT][mit] | Denis Pushkarev and contributors |
| [FastAPI](https://github.com/fastapi/fastapi) | 0.111.0 | [MIT][mit] | Sebastián Ramírez and contributors |
| [websockets](https://github.com/python-websockets/websockets) | 12.0 | [BSD-3-Clause][bsd3] | Aymeric Augustin and contributors |
| [NumPy](https://numpy.org/) | RPC: 2.0.1; SDK: ≥2.0.1 | [BSD-3-Clause][bsd3] | NumPy developers |
| [python-crontab](https://pypi.org/project/python-crontab/) | 3.2.0 | [LGPL-3.0-or-later][lgpl3] | Martin Owens and contributors |
| [Pydantic](https://github.com/pydantic/pydantic) | 2.10.6 | [MIT][mit] | Samuel Colvin and contributors |
| [Python](https://www.python.org/) | ≥3.10, &lt;3.13 | [PSF License and included notices][python] | Python Software Foundation and contributors |
| [Dynamixel SDK](https://github.com/ROBOTIS-GIT/DynamixelSDK) | RPC: —; SDK: 3.7.51 | [Apache-2.0][apache] | ROBOTIS |
| [MuJoCo](https://github.com/google-deepmind/mujoco) | — | [Apache-2.0][apache] | Google DeepMind and contributors |
| [CImg](https://cimg.eu/) | — | [CeCILL-C][cecillc] OR [CeCILL-2.1][cecill] | David Tschumperlé and contributors |
| [OSQP](https://github.com/osqp/osqp) | v1.0.0 | [Apache-2.0][apache] | OSQP developers |
| [osqp-eigen](https://github.com/robotology/osqp-eigen) | v0.10.0 | [BSD-3-Clause][bsd3] | robotology / Fondazione Istituto Italiano di Tecnologia |


## Component-specific notices

### FreeType

This software is based in part on the work of the FreeType Team.

### CImg

RB-Y1 software uses the CImg library developed by David Tschumperlé and
contributors. The applicable CeCILL license includes the original licensor's
warranty disclaimer and limitations of liability.

### Material Design Icons

The fonts, supporting code, and individual icons in `@mdi/font` are subject to
the terms identified in the distributed package's [license file][mdi].

## License information

The project and contributor names in the table do not replace original
copyright notices. Copyright notices, license copies, and applicable NOTICE
files for each distributed version remain subject to their original terms.

For FreeType and CImg, `OR` identifies alternative licenses offered upstream.
The selected license and the terms of the applicable files govern the actual
distribution.

For components subject to source availability requirements, corresponding
source and required materials must be provided in accordance with the applicable
license and distribution method. The license links and component list on this
page do not replace corresponding-source delivery or a written source offer.

[mit]: https://opensource.org/license/mit
[apache]: https://www.apache.org/licenses/LICENSE-2.0
[bsd2]: https://opensource.org/license/bsd-2-clause
[bsd3]: https://opensource.org/license/bsd-3-clause
[mpl]: https://www.mozilla.org/MPL/2.0/
[lgpl21]: https://www.gnu.org/licenses/old-licenses/lgpl-2.1.html
[lgpl3]: https://www.gnu.org/licenses/lgpl-3.0.html
[ftl]: https://spdx.org/licenses/FTL.html
[gpl2]: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html
[cecillc]: https://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html
[cecill]: https://www.cecill.info/licences/Licence_CeCILL_V2.1-en.html
[python]: https://docs.python.org/3.12/license.html
[mdi]: https://github.com/Templarian/MaterialDesign-Webfont/blob/v7.4.47/LICENSE