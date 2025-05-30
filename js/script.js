document.getElementById('excel-import').addEventListener('change', function(event) {
    const file = event.target.files[0];
    const reader = new FileReader();

    reader.onload = function(e) {
        const text = e.target.result;
        const linhas = text.split('\n').map(l => l.split(','));
        let empresa = linhas[1][0].split(";")[0];
        let tipoap = linhas[1][0].split(";")[1];
        let numap = linhas[1][0].split(";")[2];
        let fornecedor = linhas[1][0].split(";")[3];
        let comepetencia = linhas[1][0].split(";")[4];
        let vencimento = linhas[1][0].split(";")[5];
        let nomepdf = linhas[1][0].split(";")[6];
        let comentario = linhas[1][0].split(";")[7];


        console.log('Conteúdo lido:', linhas);
        console.log('Empresa:', empresa);
        console.log('Tipo de AP:', tipoap);
        console.log('Nº da AP:', numap);
        console.log('Fornecedor:', fornecedor);
        console.log('Competência:', comepetencia);
        console.log('Data de Vencimento:', vencimento);
        console.log('Nome do PDF:', nomepdf);
        console.log('Comentário:', comentario);

    };

    reader.readAsText(file);
});

const { chromium } = require('playwright');

const browser = await chromium.launch({ headless: false });
const context = await browser.newContext();
