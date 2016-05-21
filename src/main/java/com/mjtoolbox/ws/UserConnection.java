package com.mjtoolbox.ws;
import java.sql.*;


/**
 * Created by irisha on 21.05.16.
 */
public class UserConnection {
    private String currentScrean;

    public UserConnection() {

    }

    public String excuteSelect(String query) {
        try {
            //String url = "jdbc:postgresql://yuranich-server.ddns.net/postgres";
            Class.forName("org.postgresql.Driver");
            Connection conn = DriverManager.getConnection("jdbc:postgresql://localhost","postgres","");
            Statement stmt = conn.createStatement();
            ResultSet rs;
            rs = stmt.executeQuery(query);

            while ( rs.next() ) {
                String s = rs.toString();
                System.out.println(s);
                return s;
            }
            conn.close();
        } catch (Exception e) {
            System.err.println("Got an exception! ");
            System.err.println(e.getMessage());
        }
        return null;
    }

    public static void main (String[] args) {

    }

}
