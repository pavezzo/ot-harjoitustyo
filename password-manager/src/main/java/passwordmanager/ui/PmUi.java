/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package passwordmanager.ui;

import java.util.ArrayList;
import java.util.logging.Level;
import java.util.logging.Logger;
import javafx.application.Application;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.PasswordField;
import javafx.scene.control.TextField;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.GridPane;
import javafx.scene.layout.Pane;
import javafx.stage.Stage;
import passwordmanager.domain.Database;
import passwordmanager.domain.User;

/**
 *
 * @author Paavo
 */
public class PmUi extends Application {
    ArrayList<User> users = new ArrayList<>();
    Database db = new Database();
    
    @Override
    public void init() throws Exception {
        
    }

    @Override
    public void start(Stage primaryStage) throws Exception {
        //BorderPane layout = new BorderPane();
        GridPane loggedinLayout = new GridPane();
        loggedinLayout.setAlignment(Pos.CENTER);
        Label loggedinLbl = new Label("Logged id");
        loggedinLayout.add(loggedinLbl, 0, 0);
        Scene loggedinScene = new Scene(loggedinLayout, 400, 400);

        
        
        TextField usernameField = new TextField();
        PasswordField passwordField = new PasswordField();
        
        GridPane layout = new GridPane();
        layout.setAlignment(Pos.CENTER);
        Button logginBtn = new Button("Log in");
        Label createAccountLbl = new Label("Don't have an account?");
        Button createAccountScnBtn = new Button("Create account");
        
        logginBtn.setOnAction((event) -> {
            /*
            for (User user : users) {
                System.out.println(user.getUsername());
                if (user.getPassword() == passwordField.getText().trim()) {
                    primaryStage.setScene(loggedinScene);
                }
            }
            */
            User kayttaja = new User(usernameField.getText().trim(), passwordField.getText().trim());
 
           
            try {
                boolean loggedin = db.logIn(kayttaja);
                System.out.println(loggedin);
                if (loggedin) {
                    primaryStage.setScene(loggedinScene);
                }
            } catch (Exception ex) {
                
            }
            

        });

        
        layout.add(usernameField, 0, 0);
        layout.add(passwordField, 0, 1);
        layout.add(logginBtn, 0, 2);
        layout.add(createAccountLbl, 0, 3);
        layout.add(createAccountScnBtn, 0, 4);
        
        Scene scene = new Scene(layout, 400, 400);
        primaryStage.setScene(scene);
        primaryStage.show();
        
        
        GridPane createAccountLayout = new GridPane();
        createAccountLayout.setAlignment(Pos.CENTER);
        
        TextField createUsernameField = new TextField();
        PasswordField createPasswordField = new PasswordField();
        Button createUserBtn = new Button("Create new account");
        
        
        createUserBtn.setOnAction((event) -> {
            String username = createUsernameField.getText();
            String password = createPasswordField.getText();
            
            User kayttaja = new User(username, password);
            users.add(kayttaja);
            
            try {
                db.newUser(kayttaja);
            } catch (Exception ex) {
                Logger.getLogger(PmUi.class.getName()).log(Level.SEVERE, null, ex);
            }
            
            primaryStage.setScene(scene);
        });
        
        createAccountLayout.add(createUsernameField, 0, 0);
        createAccountLayout.add(createPasswordField, 0, 1);
        createAccountLayout.add(createUserBtn, 0, 2);

        
        Scene accountScn = new Scene(createAccountLayout, 400, 400);
        
        createAccountScnBtn.setOnAction((event) -> {
            primaryStage.setScene(accountScn);
        });
        

    }
    
    public static void main(String[] args) {
        launch(args);
    }
}
