//Prototype
//Cloneble->`object.clone()`によってObjectというインスタンスを複製可能
public interface Markdown extends Cloneable {
    public abstract void use(String s);
    public abstract Markdown createClone();
}