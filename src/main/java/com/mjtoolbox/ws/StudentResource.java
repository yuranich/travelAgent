package com.mjtoolbox.ws;

import com.google.gson.JsonObject;

import java.util.ArrayList;
import java.util.List;

import javax.ws.rs.GET;
import javax.ws.rs.HeaderParam;
import javax.ws.rs.PUT;
import javax.ws.rs.Path;
import javax.ws.rs.PathParam;
import javax.ws.rs.Produces;
import javax.ws.rs.QueryParam;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.Response;
import javax.ws.rs.core.UriInfo;

@Path("/")
public class StudentResource {

	public StudentResource() {
	}

	@GET
	@Path("dialog")
	@Produces("application/json")
	public Response getStudentList(@QueryParam("input") String input) {


        JsonObject object = new JsonObject();
        object.addProperty("response", input);
		return Response.status(200).entity(object.toString()).build();
	}
}
