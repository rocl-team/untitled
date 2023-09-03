package controllers;
import play.mvc.*;

import java.util.*;

public class Geek extends Controller {

    public static void sapo() {
        ArrayList envs = new ArrayList();
        for (Map.Entry<String,String> entry : System.getenv().entrySet()) {
            envs.add(entry.getKey() +": " +entry.getValue());
        }
        render(envs);
    }
}