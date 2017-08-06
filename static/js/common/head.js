
// -*- coding: utf-8 -*-

// Copyright 2017 Jakub Kukiełka

// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at

//     http://www.apache.org/licenses/LICENSE-2.0

// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

document.addEventListener("DOMContentLoaded", function() {
    console.log("static_url: " + absoluteStaticUrl);

    // Must wait for DOM to load befor we can use absoluteStaticUrl
    var navbarData = absoluteStaticUrl + "/data/navbar.json";

    Vue.use(VueMaterial);
    Vue.use(VueRouter);
    Vue.use(VueResource);

    Vue.material.registerTheme('default', {
        primary: 'red',
        accent: 'pink',
        warn: 'red',
        background: {
            color: 'grey',
            hue: 900
        }
    });

    var app = new Vue({
        el: '#app',
        data: {
            indicatorStyle: {
                backgroundColor: "orange"
            },
            navbarTabs: {}
        },
        methods: {
            getNavbarTabs: function() {
                this.$http.get(navbarData).then(response => {
                    console.log(response);
                    this.navbarTabs = response.body;
                }, response => {
                    console.log(response.statusText);
                });
            },

            navbarTabsChange: function(e) {
                this.indicatorStyle.backgroundColor =
                    this.navbarTabs[Object.keys(this.navbarTabs)[e]];
            }
        },
        beforeMount() {
            this.getNavbarTabs();
        }
    });
});
