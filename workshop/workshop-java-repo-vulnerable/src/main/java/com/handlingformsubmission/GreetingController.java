package com.handlingformsubmission;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;
//new imports
import javax.script.ScriptEngineManager;
import javax.script.ScriptEngine;
import javax.script.ScriptException;
import java.io.IOException;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@Controller
public class GreetingController {

  @GetMapping("/hello")
  public String helloForm(Model model) {
    model.addAttribute("hello", new Greeting());
    return "hello";
  }

  @PostMapping("/hello")
  public String greetingSubmit(@ModelAttribute Greeting hello, Model model) {
    model.addAttribute("hello", hello);
    return "welcome";
  }

  @GetMapping("/")
  public String index(Model model) {
    model.addAttribute("hello", new Greeting());
    return "index";
  }
  
  // new vulnerabilities
  @PostMapping("/input")
  public String Input(HttpServletRequest req, HttpServletResponse resp) throws IOException {
    String input = req.getParameter("input");
    ScriptEngineManager manager = new ScriptEngineManager();
    ScriptEngine engine = manager.getEngineByName("JavaScript");
    try {
     engine.eval(input);
    } catch (ScriptException e) {
     return "exception";
    }
    return null;
    
    //engine.eval(input); // Noncompliant
    //return "input";
  }
  
  @PostMapping("/header")
  public void header(HttpServletRequest req, HttpServletResponse resp) throws IOException {
  String value = req.getParameter("value");
  resp.addHeader("X-Header", value); // Noncompliant
  }
  
  //@GetMapping("/sqlInjection")
  //public List<User> unsafeQueryFindUserByName(@RequestParam String name) { 
  // String jql = "from User where name = '" + name + "'";
  //}

}