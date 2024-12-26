var obat = new Vue({
    el: '#obat',
    delimiters: ['[[', ']]'],
    data: {
        hasil: 'Obat',
        dataobat: ''
    },

    mounted() {
        let url = "http://127.0.0.1:8000/api/obat/";
        fetch(url)
            .then(response => response.json())
            .then(data => {
                this.dataobat = data

            })
    }
})