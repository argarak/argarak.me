
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
    // Must wait for DOM to load befor we can use absoluteStaticUrl
    var navbarData = absoluteStaticUrl + "/data/navbar.json";

    Vue.use(VueMaterial);
    Vue.use(VueResource);

    var getSubdomain = function() {
        var urlData = window.location.host.split(".");

        if(urlData.length < 3) {
            return null;
        }

        return urlData[0];
    };

    Vue.material.registerTheme('default', {
        primary: 'red',
        accent: 'pink',
        warn: 'red',
        background: {
            color: 'grey',
            hue: 900
        }
    });

    Vue.material.setCurrentTheme('default');
    
    var app = new Vue({
        el: '#app',
        data: {
            navbarTabs: {},
            navbarActiveList: []
        },
        methods: {
            getNavbarTabs: function() {
                this.$http.get(navbarData).then(response => {                     
                    this.navbarTabs = response.body;

                    this.selectTab();
                }, response => {
                    console.warn(response.statusText);
                });
            },

            navbarTabsChange: function(e) {
                this.$el.firstChild
                    .querySelector("#nav-tabs")
                    .querySelectorAll(".md-tab-indicator")[0]
                    .style.backgroundColor = this.navbarTabs[
                        Object.keys(this.navbarTabs)[e]].color;
            },

            selectTab: function() {
                var subdomain = getSubdomain();
                var keySubdomain;

                if(Object.keys(this.navbarTabs).length === 0 &&
                   this.navbarTabs.constructor === Object) {
                    console.error("Active tab could not be selected, " +
                                  "navbarTabs is empty.");
                    return false;
                }

                this.navbarActiveList = [];

                for(var i = 0; i < Object.keys(this.navbarTabs).length; ++i) {
                    this.navbarActiveList.push(false);
                }

                var index = 0;
                var self = this;

                Object.keys(this.navbarTabs).some(function(key) {
                    var url = self.navbarTabs[key].url.split('/')[2];
                    
                    // No subdomain
                    if(url.split(".").length < 3) {
                        keySubdomain = null;
                    } else {
                        keySubdomain = url.split(".")[0];
                    }

                    if(keySubdomain === subdomain) {
                        self.navbarActiveList[index] = true;
                        return true;
                    }

                    ++index;
                });

                return true;
            },
        },

        beforeMount() {
            this.getNavbarTabs();
        }
    });
});
