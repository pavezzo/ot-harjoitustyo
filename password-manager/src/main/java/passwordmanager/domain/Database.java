/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package passwordmanager.domain;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author Paavo
 */
public class Database {
    
    public Connection loadDatabase() throws Exception {
        //Class.forName("org.h2.Driver");
        Connection conn = null;
            // throws an exception if the database does not exists
        conn = DriverManager.getConnection("jdbc:sqlite:database.db");
 
        initDatabase();
        

        return conn;
    }
    
    public void initDatabase() throws SQLException {
        try (Connection conn = DriverManager.getConnection("jdbc:sqlite:database.db")) {
            conn.prepareStatement("CREATE TABLE IF NOT EXISTS User(id integer primary key not null, username varchar(255), password varchar(255));").executeUpdate();            
        } catch (SQLException e) {
            System.out.println(e);
        }
    }
    
    public void newUser(User user) throws Exception {
        Connection conn = loadDatabase();
        
        try {
            conn.prepareStatement("INSERT INTO User (username, password) "
                    + "VALUES ('" + user.getUsername() + "', '" + user.getPassword() + "');").executeUpdate();
        } catch (SQLException ex) {
            Logger.getLogger(Database.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
    
    public boolean isUser(User user) {
        Connection conn = loadDatabase();
        
        try {
            
        }
    }
}
