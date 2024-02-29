class Tv {
  brand:string;
  size:number;
  resolution:string;
  connections:string[];
  connectedTo?:string;

  constructor( brand, size,resolution,connections, connectedTo?) {
    this.brand = brand;
    this.size = size;
    this.resolution = resolution;
    this.connections = connections;
    this.connectedTo = connectedTo;

  }

  turnOn():void {
    console.log(
      `TV ${this.brand}, ${this.size}", resolution: ${this.resolution} \n\
available connections: ${this.connections}`)
  }
}

const tv1 = new Tv('aoc', 21.5, 'full hd', ['hdmi','dvi'])

tv1.turnOn();