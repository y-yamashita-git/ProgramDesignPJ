public class BulletPoint implements Markdown {
    @Override
    public void use(String string) {
        System.out.println("* " + string);
    }

    @Override
    public Markdown createClone() {
        Markdown m = null;
        try {
            m = (Markdown)clone();
        } catch (CloneNotSupportedException error) {
            error.printStackTrace();
        }
        return m;
    }

}