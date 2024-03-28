class Estudante{
  private _matricula: string;
  private _nome: string;
  private _notasProvas: number[];
  private _notasTrabalhos: number[];

  constructor(
    matricula: string, 
    nome: string, 
    notasProvas: number[], 
    notasTrabalhos: number[]) {

      this._matricula = matricula;
      this._nome = nome;
      this._notasProvas = notasProvas;
      this._notasTrabalhos = notasTrabalhos;
  }

  calcularMedia(): number {
    const somaProvas = this._notasProvas.reduce((acc, nota) => acc + nota, 0);
    const somaTrabalhos = this._notasTrabalhos.reduce((acc, nota) => acc + nota, 0);
    const totalNotas = this._notasProvas.length + this._notasTrabalhos.length;
    const valorFinal =  (somaProvas + somaTrabalhos) / totalNotas;
    console.log(valorFinal)
    return valorFinal;
  }
}

const estudante1 = new Estudante('16622','ronalty', [5,6,5,6], [5,6]);

estudante1.calcularMedia();
