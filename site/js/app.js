
const { Mask, MaskInput, vMaska } = Maska

new MaskInput("[data-maska]") // for masked input
const mask = new Mask({ mask: "#-#" }) // for programmatic use

const app = Vue.createApp({

    data() {
        return {

            mostraCadastro: false,
            mostraConsulta: false,

        }
    },

    methods: {

        toggleCadastro() {
            this.mostraCadastro = !this.mostraCadastro
            this.mostraConsulta = false
        },
        toggleConsulta() {
            this.mostraConsulta = !this.mostraConsulta
            this.mostraCadastro = false
        }

    },

    directives: { maska: vMaska },

    
})


app.mount('#app')

