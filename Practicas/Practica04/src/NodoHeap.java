import java.util.ArrayList;

public class NodoHeap{

    private NodoHeap padre;
    private int llave;
    private int grado;
    private ArrayList<NodoHeap> hijos;
    private NodoHeap sHermano;

    public NodoHeap(int llave){
        this.padre = new NodoHeap();
        this.llave = 0;
        this.grado = 0;
        this.hijos = new ArrayList<NodoHeap>();
        this.sHermano = new NodoHeap();
    }

    public void agregarHijo(NodoHeap hijo) {
        this.hijos.add(hijo);
    }

    public NodoHeap getPadre() {
        return this.padre;
    }

    public int getLlave(){
        return this.llave;
    }

    public int getGrado(){
        return this.grado;
    }

    public ArrayList<NodoHeap> getHijos(){
        return this.hijos;
    }

    public NodoHeap getSHermano(){
        return this.sHermano;
    }


    public void setPadre(NodoHeap padre) {
        this.padre = padre;
    }

    public void setLlave(int llave) {
        this.llave = llave;
    }

    public void setGrado(int grado){
        this.grado = grado;
    }

    public void setHijos(ArrayList<NodoHeap> hijos){
        this.hijos = hijos;
    }

    public void setSHermano(NodoHeap sHermano){
        this.sHermano = sHermano;
    }

}