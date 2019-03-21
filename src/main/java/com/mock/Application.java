package com.mock;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class Application {

	public static void main(String[] args) {
		System.setProperty("server.port", "8090");
		System.setProperty("management.security.enabled", "false");
		System.setProperty("security.basic.enabled", "false");
		SpringApplication.run(Application.class, args);
	}

}