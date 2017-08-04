
document.addEventListener("DOMContentLoaded", function() {
    Vue.use(VueMaterial);
    Vue.use(VueRouter);

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
            tabs: ["a", "b", "c"],
            active: true
        }
    });
});
