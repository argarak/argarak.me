
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
                console.log(e);
            }
        },
        beforeMount() {
            this.getNavbarTabs();
        }
    });
});
