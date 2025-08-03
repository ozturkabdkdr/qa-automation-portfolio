package api;

import io.restassured.http.ContentType;
import org.testng.annotations.Test;
import static io.restassured.RestAssured.*;
import static org.hamcrest.Matchers.*;

public class GetPostsTest extends BaseTest {

    @Test
    public void testGetAllPosts() {
        given()
            .when()
            .get("/posts")
            .then()
            .statusCode(200)
            .contentType(ContentType.JSON)
            .body("size()", greaterThan(0));
    }
}
