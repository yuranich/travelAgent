package com.mjtoolbox.ws;
import java.sql.*;


/**
 * Created by irisha on 21.05.16.
 */
public class UserConnection {
    private String currentScrean;

    public UserConnection() {

    }

    public String getAppReaction(String userReaction) {
        return null;
    }

    public static void main (String[] args) {
        String query = "Select * from SESSION";
        try {
            String url = "jdbc:postgresql://yuranich-server.ddns.net/postgres";

            Connection conn = DriverManager.getConnection(url,"","");
            Statement stmt = conn.createStatement();
            ResultSet rs;
            rs = stmt.executeQuery(query);

            while ( rs.next() ) {
                String s = rs.toString();
                System.out.println(s);
            }
            conn.close();
        } catch (Exception e) {
            System.err.println("Got an exception! ");
            System.err.println(e.getMessage());
        }
    }

}
