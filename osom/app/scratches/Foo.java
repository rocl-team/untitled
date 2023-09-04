package scratches;

import java.util.Map;

public class Foo {
    public static void main(String[] args) {
        for (int i=0;i < args.length;i++) {
            System.out.println("Hey! " + args[i]);
        }
        for (Map.Entry<String,String> e: System.getenv().entrySet()) {
            System.out.println(e.getKey() +": "+e.getValue());
        }

    }
}