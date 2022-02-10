package Controladores;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
public class HomeControlador {

    @RequestMapping("/login")
    public String login(){
        return login() ;
    }
    @RequestMapping("/")
    public String index(){
        return index();
    }
    @RequestMapping("/criar_bot")
    public String criar_bot(){
        return criar_bot();
    }
    @RequestMapping("/relatorio")
    public String relatorio(){
        return relatorio();
    }
}
